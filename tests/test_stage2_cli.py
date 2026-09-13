from pathlib import Path
import re
import subprocess
import sys
import unittest

from stage2_support import program


ROOT = Path(__file__).resolve().parents[1]
EXTENSIONS = "#references, #sequencing, #panic, #exceptions"


class Stage2CliTests(unittest.TestCase):
    def test_first_error_and_exit_code(self):
        cases = [
            ("throw(0)", "", "ERROR_EXCEPTION_TYPE_NOT_DECLARED"),
            ("let x = throw(0) in n", "exception type = Nat", "ERROR_AMBIGUOUS_THROW_TYPE"),
            ("let r = <0xabc> in n", "", "ERROR_AMBIGUOUS_REFERENCE_TYPE"),
            ("let x = panic! in n", "", "ERROR_AMBIGUOUS_PANIC_TYPE"),
            ("*0", "", "ERROR_NOT_A_REFERENCE"),
            ("<0xabc>", "", "ERROR_UNEXPECTED_MEMORY_ADDRESS"),
            ("new(unknown)", "", "ERROR_UNEXPECTED_REFERENCE"),
        ]
        for body, declarations, code in cases:
            with self.subTest(code=code):
                source = program(body, declarations=declarations, extensions=EXTENSIONS)
                result = subprocess.run([sys.executable, str(ROOT / "main.py")],
                                        input=source, capture_output=True, text=True, timeout=10)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertEqual(re.findall(r"ERROR_[A-Z_]+", result.stderr), [code])
                self.assertNotIn("Traceback", result.stderr)

    def test_combined_program(self):
        source = program(
            "let r = new(n) in ((r := succ(*r)); "
            "try { if Nat::iszero(*r) then throw(*r) else *r } catch { x => x })",
            declarations="exception type = Nat", extensions=EXTENSIONS,
        )
        result = subprocess.run([sys.executable, str(ROOT / "main.py")],
                                input=source, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, "")

    def test_unsupported_modes(self):
        flags = ("#structural-subtyping", "#ambiguous-type-as-bottom",
                 "#type-reconstruction", "#universal-types")
        for flag in flags:
            with self.subTest(flag=flag):
                result = subprocess.run([sys.executable, str(ROOT / "main.py")],
                                        input=program("n", extensions=flag),
                                        capture_output=True, text=True, timeout=10)
                self.assertEqual(result.returncode, 3, result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertIn("UNSUPPORTED_FEATURE", result.stderr)
                self.assertIn(flag, result.stderr)
                self.assertNotIn("Traceback", result.stderr)
