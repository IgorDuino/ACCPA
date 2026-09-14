from pathlib import Path
import subprocess
import sys
import unittest

from stella_checker.checker import check_program
from stella_checker.errors import TypeCheckError
from stella_checker.syntax.parsing import parse_program


ROOT = Path(__file__).resolve().parents[1]


def program(body: str, result: str = "Nat", parameter: str = "n : Nat",
            declarations: str = "", extensions: str = "") -> str:
    flags = f"extend with {extensions};\n" if extensions else ""
    return f"language core;\n{flags}{declarations}\nfn main({parameter}) -> {result} {{ return {body} }}"


def run_cli(source: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(ROOT / "main.py")],
                          input=source, capture_output=True, text=True, timeout=10)


class CheckerTestCase(unittest.TestCase):
    def assert_valid(self, source: str) -> None:
        check_program(parse_program(source))

    def assert_error(self, source: str, code: str) -> None:
        with self.assertRaises(TypeCheckError) as raised:
            check_program(parse_program(source))
        self.assertEqual(raised.exception.code, code)
