from stage2_support import ProgramTests, program


EXTENSIONS = "#references, #sequencing"


class ReferenceTests(ProgramTests):
    def test_valid(self):
        cases = [
            ("allocation", "new(n)", "&Nat", "n : Nat"),
            ("infer_and_read", "let r = new(n) in *r", "Nat", "n : Nat"),
            ("assignment", "r := 0", "Unit", "r : &Nat"),
            ("write_then_read", "let r = new(n) in ((r := succ(n)); *r)", "Nat", "n : Nat"),
            ("expected_allocation", "new([])", "&[Nat]", "n : Nat"),
            ("expected_assignment", "r := []", "Unit", "r : &[Nat]"),
            ("function_reference", "new(fn(x : Nat) { return x })", "&(fn(Nat) -> Nat)", "n : Nat"),
            ("nested_reference", "new(new(n))", "&(&Nat)", "n : Nat"),
            ("memory_uppercase", "<0xBEEF>", "&Nat", "n : Nat"),
            ("memory_ascription", "let r = <0xabc> as &Nat in *r", "Nat", "n : Nat"),
            ("memory_dereference", "*<0xabc>", "Nat", "n : Nat"),
            ("expected_dereference", "*new([])", "[Nat]", "n : Nat"),
            ("conditional_memory_dereference", "*(if true then <0xa> else <0xb>)", "Nat", "n : Nat"),
            ("record_field_order", "r", "&{a : Nat, b : Bool}", "r : &{b : Bool, a : Nat}"),
        ]
        for name, body, result, parameter in cases:
            with self.subTest(case=name):
                self.assert_valid(program(body, result, parameter, extensions=EXTENSIONS))

    def test_errors(self):
        cases = [
            ("read_nonreference", "*0", "Nat", "n : Nat", "ERROR_NOT_A_REFERENCE"),
            ("assignment_before_rhs", "n := unknown", "Unit", "n : Nat", "ERROR_NOT_A_REFERENCE"),
            ("unexpected_allocation_before_operand", "new(unknown)", "Nat", "n : Nat", "ERROR_UNEXPECTED_REFERENCE"),
            ("wrong_allocation_payload", "new(true)", "&Nat", "n : Nat", "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("wrong_dereferenced_payload", "*new(true)", "Nat", "n : Nat", "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("wrong_assignment_payload", "r := true", "Unit", "r : &Nat", "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("assignment_result", "r := 0", "Nat", "r : &Nat", "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("reference_content_equality", "r", "&Nat", "r : &Bool", "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("memory_ambiguous", "let r = <0xabc> in n", "Nat", "n : Nat", "ERROR_AMBIGUOUS_REFERENCE_TYPE"),
            ("assignment_does_not_infer_from_rhs", "<0xa> := 0", "Unit", "n : Nat", "ERROR_AMBIGUOUS_REFERENCE_TYPE"),
            ("memory_unexpected", "<0xabc>", "Nat", "n : Nat", "ERROR_UNEXPECTED_MEMORY_ADDRESS"),
            ("no_record_width_subtyping", "r", "&{a : Nat}", "r : &{a : Nat, b : Bool}", "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("allocation_does_not_resolve_empty_list", "let r = new([]) in n", "Nat", "n : Nat", "ERROR_AMBIGUOUS_LIST_TYPE"),
        ]
        for name, body, result, parameter, code in cases:
            with self.subTest(case=name):
                self.assert_error(program(body, result, parameter, extensions=EXTENSIONS), code)
