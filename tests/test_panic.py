from stage2_support import ProgramTests, program


EXTENSIONS = "#panic, #sequencing, #exceptions"


class PanicTests(ProgramTests):
    def test_valid(self):
        cases = [
            ("expected_nat", "panic!", "Nat"),
            ("expected_function", "panic!", "fn(Nat) -> Nat"),
            ("argument_expected", "succ(panic!)", "Nat"),
            ("sequence_expected_unit", "panic!; n", "Nat"),
            ("handler_expected", "let x = try { 0 } with { panic! } in x", "Nat"),
        ]
        for name, body, result in cases:
            with self.subTest(case=name):
                self.assert_valid(program(body, result, extensions=EXTENSIONS))

    def test_ambiguity(self):
        for body in ("let x = panic! in n", "let f = fn(x : Nat) { return panic! } in n"):
            with self.subTest(body=body):
                self.assert_error(program(body, extensions=EXTENSIONS), "ERROR_AMBIGUOUS_PANIC_TYPE")
