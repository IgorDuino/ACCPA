import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "tests" / "hw1"


def dataset_paths(group):
    paths = DATA.glob("*.in" if group == "all" else f"{group}-*.in")
    return sorted(paths, key=lambda p: (p.stem.split("-")[0], int(p.stem.split("-")[1])))


def check_case(path):
    expected = path.with_suffix(".out").read_text().split()
    result = subprocess.run([sys.executable, str(ROOT / "main.py"), str(path)],
                            capture_output=True, text=True, timeout=10)
    codes = re.findall(r"ERROR_[A-Z_]+", result.stderr)
    if expected:
        passed = result.returncode == 1 and len(codes) == 1 and codes[0] in expected
    else:
        passed = result.returncode == 0 and result.stderr == ""
    passed = passed and result.stdout == "" and "Traceback" not in result.stderr
    return {"name": path.stem, "expected": expected, "exit_code": result.returncode,
            "codes": codes, "passed": passed, "stderr": result.stderr}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--group", choices=("main", "extra", "all"), default="main")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    paths = dataset_paths(args.group)
    if not paths:
        parser.error(f"No dataset inputs in {DATA}")
    cases = []
    stats = Counter()
    for path in paths:
        case = check_case(path)
        cases.append(case)
        group = path.stem.split("-")[0]
        stats[f"{group}_{'pass' if case['passed'] else 'fail'}"] += 1
        if not case["passed"]:
            print(path.stem, "expected:", case["expected"] or ["OK"],
                  "actual:", case["codes"] or [case["stderr"].strip() or "OK"])
    print(dict(stats))
    if args.report:
        args.report.write_text(json.dumps({"counts": dict(stats), "cases": cases},
                                         ensure_ascii=False, indent=2) + "\n")
    return 0 if all(case["passed"] for case in cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
