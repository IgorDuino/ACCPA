import unittest

from stella_checker.checker import check_program
from stella_checker.errors import TypeCheckError
from stella_checker.syntax.parsing import parse_program


def program(body, result="Nat", parameter="n : Nat", declarations="", extensions=""):
    flags = f"extend with {extensions};\n" if extensions else ""
    return f"language core;\n{flags}{declarations}\nfn main({parameter}) -> {result} {{ return {body} }}"


class ProgramTests(unittest.TestCase):
    def assert_valid(self, source):
        check_program(parse_program(source))

    def assert_error(self, source, code):
        with self.assertRaises(TypeCheckError) as raised:
            check_program(parse_program(source))
        self.assertEqual(raised.exception.code, code)
