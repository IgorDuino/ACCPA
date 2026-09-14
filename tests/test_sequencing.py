from helpers import CheckerTestCase, program


class SequencingTests(CheckerTestCase):
    def test_valid(self):
        cases = [
            ("two_expressions", "unit; n", "Nat"),
            ("three_expressions", "unit; unit; n", "Nat"),
            ("trailing_semicolon", "unit; n;", "Nat"),
            ("expected_list", "unit; []", "[Nat]"),
            ("inferred_result", "let x = (unit; n) in x", "Nat"),
        ]
        for name, body, result in cases:
            with self.subTest(case=name):
                self.assert_valid(program(body, result, extensions="#sequencing"))

    def test_errors(self):
        cases = [
            ("first_operand_before_second", "0; unknown", "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("wrong_result", "unit; true", "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION"),
            ("let_scope", "(let x = unit in x); x", "ERROR_UNDEFINED_VARIABLE"),
        ]
        for name, body, code in cases:
            with self.subTest(case=name):
                self.assert_error(program(body, extensions="#sequencing"), code)
