import re
import unittest

from stella_checker.checker import check_main, check_program
from stella_checker.errors import TypeCheckError
from stella_checker.syntax.parsing import parse_program
from stella_checker.types import NAT

from helpers import ROOT, CheckerTestCase, program, run_cli


VALID = [
    ("zero", program("0")),
    ("positive_literal", program("123")),
    ("bool_main", program("b", "Bool", "b : Bool")),
    ("unit", program("unit", "Unit")),
    ("pred", program("Nat::pred(n)")),
    ("if", program("if Nat::iszero(n) then 0 else succ(n)")),
    ("higher_order", program("fn(f : fn(Nat) -> Nat) { return fn(x : Nat) { return f(f(x)) } }",
                             "fn(fn(Nat) -> Nat) -> fn(Nat) -> Nat")),
    ("lambda_application", program("(fn(x : Nat) { return succ(x) })(n)")),
    ("lambda_shadow", program("fn(n : Bool) { return n }", "fn(Bool) -> Bool")),
    ("lambda_does_not_leak", program("{fn(n : Bool) { return n }, n}", "{fn(Bool) -> Bool, Nat}")),
    ("empty_tuple", program("{}", "{}")),
    ("tuple", program("{true, 0, unit}", "{Bool, Nat, Unit}")),
    ("tuple_projection", program("{true, {0, false}}.2.1")),
    ("record_reorder", program("{b = true, a = n}", "{a : Nat, b : Bool}")),
    ("record_type_reorder", program("r", "{a : Nat, b : Bool}", "r : {b : Bool, a : Nat}")),
    ("record_access", program("{a = 0, b = false}.a")),
    ("let_shadow_rhs", program("let n = succ(n) in n")),
    ("let_does_not_leak", program("{let n = true in n, n}", "{Bool, Nat}")),
    ("let_bindings", program("let x = 0, y = succ(x) in y")),
    ("ascription", program("(n as Nat)")),
    ("sum_left", program("inl(n)", "Nat + Bool")),
    ("sum_right", program("inr(true)", "Nat + Bool")),
    ("sum_conditional", program("if true then inl(n) else inr(false)", "Nat + Bool")),
    ("sum_argument", program("f(inl(n))", declarations="fn f(s : Nat + Bool) -> Nat { return 0 }")),
    ("sum_ascription", program("let s = inl(n) as (Nat + Bool) in match s { inl(x) => x | inr(b) => 0 }")),
    ("sum_match", program("match s { inl(x) => x | inr(b) => if b then 0 else 1 }",
                          parameter="s : Nat + Bool")),
    ("match_expected", program("match s { inl(x) => inl(x) | inr(b) => inr(b) }", "Nat + Bool", "s : Nat + Bool")),
    ("match_shadow", program("match s { inl(s) => s | inr(s) => if s then 0 else 1 }", parameter="s : Nat + Bool")),
    ("match_catchall", program("match s { x => x }", "Nat + Bool", "s : Nat + Bool")),
    ("nested_sum", program("match s { inl(x) => x | inr(inl(b)) => 0 | inr(inr(n)) => n }",
                           parameter="s : Nat + (Bool + Nat)")),
    ("variant", program("<| ok = n |>", "<| ok : Nat, error : Bool |>")),
    ("variant_match", program("match v { <| ok = x |> => x | <| error = b |> => 0 }", parameter="v : <| ok : Nat, error : Bool |>")),
    ("variant_reorder", program("v", "<| ok : Nat, error : Bool |>", "v : <| error : Bool, ok : Nat |>")),
    ("empty_list_expected", program("[]", "[Nat]")),
    ("head_empty_expected", program("List::head([])")),
    ("nonempty_list_infer", program("let xs = [0, n] in List::head(xs)")),
    ("cons_infer", program("let xs = cons(n, []) in List::head(xs)")),
    ("tail", program("List::tail([0, n])", "[Nat]")),
    ("isempty", program("List::isempty([] as [Nat])", "Bool")),
    ("nested_list", program("[[], [0]]", "[[Nat]]")),
    ("list_sums", program("[inl(n), inr(true)]", "[Nat + Bool]")),
    ("record_expected", program("{s = inl(n), xs = []}", "{s : Nat + Bool, xs : [Bool]}")),
    ("nat_rec", program("Nat::rec(n, 0, fn(i : Nat) { return fn(r : Nat) { return succ(r) } })")),
    ("nat_rec_bool", program("Nat::rec(n, true, fn(i : Nat) { return fn(r : Bool) { return r } })", "Bool")),
    ("nat_rec_expected_list", program("Nat::rec(n, [], fn(i : Nat) { return fn(xs : [Nat]) { return cons(i, xs) } })", "[Nat]")),
    ("nat_rec_inferred", program("let r = Nat::rec(n, 0, fn(i : Nat) { return fn(x : Nat) { return succ(x) } }) in r")),
    ("if_inferred", program("let x = if true then 0 else n in x")),
    ("match_inferred", program("let x = match s { inl(n) => n | inr(b) => 0 } in x", parameter="s : Nat + Bool")),
    ("fix_function_variable", program("fix(f)", parameter="f : fn(Nat) -> Nat")),
    ("fix", program("fix(fn(self : fn(Nat) -> Nat) { return fn(x : Nat) { return self(x) } })(n)")),
    ("fix_expected_sum", program("fix(fn(s : Nat + Bool) { return inl(n) })", "Nat + Bool")),
    ("fix_expected_list", program("fix(fn(xs : [Nat]) { return [] })", "[Nat]")),
    ("trailing_semicolon", program("n;")),
    ("unused_good_function", program("n", declarations="fn unused(x : Bool) -> Bool { return x }")),
    ("forward_function", program("later(n)") + "\nfn later(x : Nat) -> Nat { return succ(x) }"),
    ("nested_function", "language core; fn main(n : Nat) -> Nat { fn inner(x : Nat) -> Nat { return succ(x) } return inner(n) }"),
    ("two_arguments", program("f(0, true)", declarations="fn f(x : Nat, b : Bool) -> Nat { return x }")),
]

INVALID = [
    ("missing_main", "language core;", "ERROR_MISSING_MAIN"),
    ("undefined", program("unknown"), "ERROR_UNDEFINED_VARIABLE"),
    ("negative", program("-1"), "ERROR_ILLEGAL_NEGATIVE_LITERAL"),
    ("wrong_result", program("true"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("not_function", program("0(unknown)"), "ERROR_NOT_A_FUNCTION"),
    ("not_tuple", program("true.1"), "ERROR_NOT_A_TUPLE"),
    ("not_record", program("0.field"), "ERROR_NOT_A_RECORD"),
    ("not_list", program("List::head(0)"), "ERROR_NOT_A_LIST"),
    ("unexpected_lambda", program("fn(x : Nat) { return unknown }"), "ERROR_UNEXPECTED_LAMBDA"),
    ("wrong_parameter", program("fn(x : Bool) { return unknown }", "fn(Nat) -> Nat"), "ERROR_UNEXPECTED_TYPE_FOR_PARAMETER"),
    ("unexpected_tuple", program("{unknown, 0}"), "ERROR_UNEXPECTED_TUPLE"),
    ("unexpected_record", program("{a = unknown}"), "ERROR_UNEXPECTED_RECORD"),
    ("unexpected_variant", program("<| ok = unknown |>"), "ERROR_UNEXPECTED_VARIANT"),
    ("unexpected_list", program("[unknown]"), "ERROR_UNEXPECTED_LIST"),
    ("unexpected_injection", program("inl(unknown)"), "ERROR_UNEXPECTED_INJECTION"),
    ("missing_fields", program("{a = unknown}", "{a : Nat, b : Bool}"), "ERROR_MISSING_RECORD_FIELDS"),
    ("extra_fields", program("{a = 0, b = unknown}", "{a : Nat}"), "ERROR_UNEXPECTED_RECORD_FIELDS"),
    ("bad_access", program("{a = 0}.b"), "ERROR_UNEXPECTED_FIELD_ACCESS"),
    ("bad_variant_label", program("<| nope = unknown |>", "<| ok : Nat |>"), "ERROR_UNEXPECTED_VARIANT_LABEL"),
    ("missing_variant_labels", program("v", "<| a : Nat, b : Bool |>", "v : <| a : Nat |>"), "ERROR_MISSING_VARIANT_LABELS"),
    ("tuple_index", program("{0, true}.3"), "ERROR_TUPLE_INDEX_OUT_OF_BOUNDS"),
    ("tuple_length", program("{unknown}", "{Nat, Bool}"), "ERROR_UNEXPECTED_TUPLE_LENGTH"),
    ("ambiguous_sum", program("let s = inl(0) in 0"), "ERROR_AMBIGUOUS_SUM_TYPE"),
    ("ambiguous_variant", program("let v = <| a = 0 |> in 0"), "ERROR_AMBIGUOUS_VARIANT_TYPE"),
    ("ambiguous_list", program("let xs = [] in 0"), "ERROR_AMBIGUOUS_LIST_TYPE"),
    ("empty_match", program("match n {}"), "ERROR_ILLEGAL_EMPTY_MATCHING"),
    ("nonexhaustive", program("match s { inl(x) => 0 }", parameter="s : Nat + Bool"), "ERROR_NONEXHAUSTIVE_MATCH_PATTERNS"),
    ("wrong_pattern", program("match n { inl(x) => 0 }"), "ERROR_UNEXPECTED_PATTERN_FOR_TYPE"),
    ("duplicate_record", program("{a = unknown, a = 0}", "{a : Nat}"), "ERROR_DUPLICATE_RECORD_FIELDS"),
    ("duplicate_record_type", program("n", parameter="n : {a : Nat, a : Bool}"), "ERROR_DUPLICATE_RECORD_TYPE_FIELDS"),
    ("duplicate_variant_type", program("n", parameter="n : <| a : Nat, a : Bool |>"), "ERROR_DUPLICATE_VARIANT_TYPE_FIELDS"),
    ("if_condition", program("if 0 then unknown else 0"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("if_branch", program("if true then 0 else false"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("unreachable_bad_branch", program("if true then 0 else unknown"), "ERROR_UNDEFINED_VARIABLE"),
    ("succ_bool", program("succ(false)"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("pred_bool", program("Nat::pred(false)"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("iszero_bool", program("Nat::iszero(false)", "Bool"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("self_application", program("fn(x : fn(Nat) -> Nat) { return x(x) }", "fn(fn(Nat) -> Nat) -> Nat"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("parameter_not_in_scope", program("{fn(x : Nat) { return x }, x}", "{fn(Nat) -> Nat, Nat}"), "ERROR_UNDEFINED_VARIABLE"),
    ("let_rhs_not_recursive", program("let x = x in x"), "ERROR_UNDEFINED_VARIABLE"),
    ("let_scope", program("{let x = 0 in x, x}", "{Nat, Nat}"), "ERROR_UNDEFINED_VARIABLE"),
    ("branch_scope", program("match s { inl(x) => x | inr(y) => x }", parameter="s : Nat + Bool"), "ERROR_UNDEFINED_VARIABLE"),
    ("other_function_parameter", program("x", declarations="fn f(x : Nat) -> Nat { return x }"), "ERROR_UNDEFINED_VARIABLE"),
    ("unused_bad_function", program("n", declarations="fn f(x : Nat) -> Nat { return false }"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("ascription_is_checked", program("true as Nat"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("injection_payload", program("inl(true)", "Nat + Bool"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("variant_payload", program("<| a = true |>", "<| a : Nat |>"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("variant_match_missing", program("match v { <| a = x |> => x }", parameter="v : <| a : Nat, b : Bool |>"), "ERROR_NONEXHAUSTIVE_MATCH_PATTERNS"),
    ("variant_bad_pattern", program("match v { <| b = x |> => 0 }", parameter="v : <| a : Nat |>"), "ERROR_UNEXPECTED_PATTERN_FOR_TYPE"),
    ("match_result", program("match s { inl(x) => x | inr(b) => b }", parameter="s : Nat + Bool"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("nested_nonexhaustive", program("match s { inl(x) => x | inr(inl(b)) => 0 }", parameter="s : Nat + (Bool + Nat)"), "ERROR_NONEXHAUSTIVE_MATCH_PATTERNS"),
    ("homogeneous_list", program("[0, true]", "[Nat]"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("cons_tail", program("cons(0, true)", "[Nat]"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("unexpected_cons", program("cons(unknown, unknown)"), "ERROR_UNEXPECTED_LIST"),
    ("tail_not_list", program("List::tail(true)", "[Nat]"), "ERROR_NOT_A_LIST"),
    ("isempty_not_list", program("List::isempty(0)", "Bool"), "ERROR_NOT_A_LIST"),
    ("head_empty_ambiguous", program("let x = List::head([]) in 0"), "ERROR_AMBIGUOUS_LIST_TYPE"),
    ("fix_not_function", program("fix(0)"), "ERROR_NOT_A_FUNCTION"),
    ("fix_wrong_endomorphism", program("fix(fn(x : Nat) { return true })"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("rec_wrong_input", program("Nat::rec(true, 0, unknown)"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("rec_wrong_step", program("Nat::rec(n, 0, fn(i : Bool) { return unknown })"), "ERROR_UNEXPECTED_TYPE_FOR_PARAMETER"),
    ("zero_index", program("{0}.0"), "ERROR_TUPLE_INDEX_OUT_OF_BOUNDS"),
    ("missing_main_with_function", "language core; fn f(n : Nat) -> Nat { return n }", "ERROR_MISSING_MAIN"),
    ("wrong_main_arity", "language core; fn main() -> Nat { return 0 }", "ERROR_INCORRECT_ARITY_OF_MAIN"),
    ("wrong_call_arity", program("f(0, true)", declarations="fn f(n : Nat) -> Nat { return n }"), "ERROR_INCORRECT_NUMBER_OF_ARGUMENTS"),
    ("wrong_lambda_arity", program("fn() { return unknown }", "fn(Nat) -> Nat"), "ERROR_UNEXPECTED_NUMBER_OF_PARAMETERS_IN_LAMBDA"),
    ("fix_variable_not_function", program("fix(n)"), "ERROR_NOT_A_FUNCTION"),
    ("fix_variable_wrong_result", program("fix(f)", parameter="f : fn(Nat) -> Bool"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("duplicate_inferred_record", program("let r = {a = 0, a = true} in 0"), "ERROR_DUPLICATE_RECORD_FIELDS"),
    ("nested_duplicate_type", program("[]", "[{a : Nat, a : Bool}]"), "ERROR_DUPLICATE_RECORD_TYPE_FIELDS"),
    ("wrong_list_element_inferred", program("let xs = [0, false] in 0"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("wrong_sum_side", program("inr(0)", "Nat + Bool"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("wrong_tuple_element", program("{false, 0}", "{Nat, Nat}"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("wrong_record_element", program("{a = false}", "{a : Nat}"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("wrong_variant_field_type", program("v", "<| a : Bool |>", "v : <| a : Nat |>"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("extra_variant_type_label", program("v", "<| a : Nat |>", "v : <| a : Nat, b : Bool |>"), "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
    ("duplicate_branch_not_exhaustive", program("match s { inl(x) => 0 | inl(y) => 0 }", parameter="s : Nat + Bool"), "ERROR_NONEXHAUSTIVE_MATCH_PATTERNS"),
]


class CheckerTests(CheckerTestCase):
    def test_valid_programs(self):
        for name, source in VALID:
            with self.subTest(case=name):
                self.assert_valid(source)

    def test_first_error_for_invalid_programs(self):
        for name, source, code in INVALID:
            with self.subTest(case=name):
                self.assert_error(source, code)

    def test_main_type_guard(self):


        with self.assertRaises(TypeCheckError) as raised:
            check_main({"main": NAT}, None)
        self.assertEqual(raised.exception.code, "ERROR_INCORRECT_TYPE_OF_MAIN")

    def test_positive_example_files(self):
        negative = {"negative-literal.stella", "syntax-error.stella", "type-error.stella", "ambiguous-sum.stella"}
        for path in sorted((ROOT / "tests" / "examples").glob("*.stella")):
            if path.name not in negative:
                with self.subTest(file=path.name):
                    self.assert_valid(path.read_text())

    def test_cli_first_error_and_exit_code(self):
        for name, source, code in INVALID:
            with self.subTest(case=name):
                result = run_cli(source)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertEqual(re.findall(r"ERROR_[A-Z_]+", result.stderr), [code])
                self.assertNotIn("Traceback", result.stderr)

    def test_cli_valid_stdin(self):
        result = run_cli(program("succ(n)"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, "")

    def test_diagnostic_has_context(self):
        with self.assertRaises(TypeCheckError) as raised:
            check_program(parse_program(program("true")))
        message = str(raised.exception)
        for text in ("Expected Nat", "found Bool", "function main", "expression: true", "at 3:"):
            self.assertIn(text, message)


if __name__ == "__main__":
    unittest.main()
