import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from test_checker import INVALID, VALID

IMAGE = "fizruk/stella@sha256:0bc37cc4f5e328dd3812ef6b525d1e65243388a5145ea83bb77fd8196588d74b"
FLAGS = """extend with #natural-literals, #unit-type, #tuples, #records,
#let-bindings, #type-ascriptions, #sum-types, #variants, #lists,
#fixpoint-combinator, #nested-function-declarations, #multiparameter-functions,
#nullary-functions, #structural-patterns, #general-recursion, #predecessor,
#let-many-bindings;"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()
    results = []
    cases = [(name, source, None) for name, source in VALID] + INVALID
    for name, source, code in cases:
        source = source.replace("language core;", "language core;\n" + FLAGS, 1)
        result = subprocess.run(["docker", "run", "--rm", "--network", "none", "-i", IMAGE, "typecheck"],
                                input=source, text=True, capture_output=True, timeout=30)
        codes = sorted(set(re.findall(r"ERROR_[A-Z_]+", result.stdout + result.stderr)))
        acceptance_matches = (result.returncode == 0) == (code is None)
        diagnostics_match = code is None or code in codes
        status = "match" if acceptance_matches and diagnostics_match else "difference"
        results.append({"name": name, "expected": code, "reference_exit": result.returncode,
                        "reference_codes": codes, "status": status,
                        "output": result.stdout + result.stderr})
        if status == "difference":
            print(name, "expected", code, "reference", result.returncode, codes, flush=True)
    output = {"image": IMAGE, "counts": dict(Counter(r["status"] for r in results)), "cases": results}
    if args.output:
        args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(output["counts"])
    return 0 if all(r["status"] == "match" for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
