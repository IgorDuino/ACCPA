from stage2_support import ProgramTests, program


EXTENSIONS = "#exceptions, #sum-types, #variants, #tuples"


def exception_program(body, result="Nat", parameter="n : Nat", exception_type="Nat", declarations=""):
    exception = f"exception type = {exception_type}\n" if exception_type else ""
    return program(body, result, parameter, exception + declarations, EXTENSIONS)


class ExceptionTests(ProgramTests):
    def test_valid(self):
        cases = [
            ("payload_and_result_differ", "try { throw(n) } with { true }", "Bool", "n : Nat", "Nat", ""),
            ("try_with_without_exception_type", "try { n } with { 0 }", "Nat", "n : Nat", None, ""),
            ("partial_nat_catch", "try { throw(n) } catch { 0 => false }", "Bool", "n : Nat", "Nat", ""),
            ("partial_true_catch", "try { throw(false) } catch { true => 0 }", "Nat", "n : Nat", "Bool", ""),
            ("partial_false_catch", "try { throw(true) } catch { false => 0 }", "Nat", "n : Nat", "Bool", ""),
            ("unit_catch", "try { throw(unit) } catch { unit => n }", "Nat", "n : Nat", "Unit", ""),
            ("partial_successor_catch", "try { throw(n) } catch { succ(k) => k }", "Nat", "n : Nat", "Nat", ""),
            ("partial_nested_literal_catch", "try { throw(inl(n)) } catch { inl(0) => n }", "Nat", "n : Nat", "Nat + Bool", ""),
            ("partial_sum_catch", "try { throw(inr(true)) } catch { inl(x) => x }", "Nat", "n : Nat", "Nat + Bool", ""),
            ("partial_variant_catch", "try { throw(<| bad = true |>) } catch { <| ok = x |> => x }", "Nat", "n : Nat", "<| ok : Nat, bad : Bool |>", ""),
            ("catch_shadowing", "{try { 0 } catch { n => n }, n}", "{Nat, Bool}", "n : Bool", "Nat", ""),
            ("exception_visible_in_function", "try { helper(n) } catch { x => x }", "Nat", "n : Nat", "Nat", "fn helper(x : Nat) -> Nat { return throw(x) }"),
        ]
        for name, body, result, parameter, exception_type, declarations in cases:
            with self.subTest(case=name):
                self.assert_valid(exception_program(body, result, parameter, exception_type, declarations))

    def test_errors(self):
        cases = [
            ("missing_before_payload", "throw(unknown)", "Nat", None, "ERROR_EXCEPTION_TYPE_NOT_DECLARED"),
            ("catch_requires_declaration", "try { n } catch { x => n }", "Nat", None, "ERROR_EXCEPTION_TYPE_NOT_DECLARED"),
            ("wrong_try_before_missing_declaration", "try { true } catch { x => n }", "Nat", None, "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("undefined_try_before_missing_declaration", "let x = try { missing } catch { e => n } in x", "Nat", None, "ERROR_UNDEFINED_VARIABLE"),
            ("wrong_payload", "throw(true)", "Nat", "Nat", "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("undefined_payload_before_ambiguity", "let x = throw(unknown) in n", "Nat", "Nat", "ERROR_UNDEFINED_VARIABLE"),
            ("wrong_payload_before_ambiguity", "let x = throw(true) in n", "Nat", "Nat", "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("ambiguous_throw", "let x = throw(0) in n", "Nat", "Nat", "ERROR_AMBIGUOUS_THROW_TYPE"),
            ("with_does_not_infer_from_fallback", "let x = try { throw(0) } with { 0 } in x", "Nat", "Nat", "ERROR_AMBIGUOUS_THROW_TYPE"),
            ("catch_does_not_infer_from_fallback", "let x = try { throw(0) } catch { e => e } in x", "Nat", "Nat", "ERROR_AMBIGUOUS_THROW_TYPE"),
            ("wrong_handler_result", "try { 0 } catch { x => true }", "Nat", "Nat", "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("wrong_pattern", "try { 0 } catch { inl(x) => 0 }", "Nat", "Nat", "ERROR_UNEXPECTED_PATTERN_FOR_TYPE"),
            ("binding_not_in_try", "try { x } catch { x => x }", "Nat", "Nat", "ERROR_UNDEFINED_VARIABLE"),
            ("binding_does_not_leak", "{try { 0 } catch { x => x }, x}", "{Nat, Nat}", "Nat", "ERROR_UNDEFINED_VARIABLE"),
        ]
        for name, body, result, exception_type, code in cases:
            with self.subTest(case=name):
                self.assert_error(exception_program(body, result, exception_type=exception_type), code)

    def test_exception_type_does_not_leak_between_programs(self):
        self.assert_valid(exception_program("throw(0)"))
        self.assert_error(exception_program("throw(0)", exception_type=None), "ERROR_EXCEPTION_TYPE_NOT_DECLARED")
        self.assert_valid(exception_program("throw(true)", exception_type="Bool"))

    def test_declarations(self):
        self.assert_valid(program("throw(n)", extensions=EXTENSIONS) + "\nexception type = Nat")
        self.assert_valid(
            "language core; extend with #exceptions; exception type = Nat "
            "fn main(n : Nat) -> Nat { "
            "fn inner(x : Nat) -> Nat { return throw(x) } "
            "return try { inner(n) } catch { e => e } }"
        )
        self.assert_error(exception_program("n", declarations="exception type = Bool"),
                          "ERROR_DUPLICATE_EXCEPTION_TYPE")
        self.assert_error(exception_program(
            "n", declarations="fn helper(x : Nat) -> Nat { exception type = Bool return x }",
        ), "ERROR_ILLEGAL_LOCAL_EXCEPTION_TYPE")
