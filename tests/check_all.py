import argparse
import json
from pathlib import Path

from check_hw1 import ROOT, check_case, dataset_paths


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hw", nargs="+", choices=("hw1", "hw2", "hw3"),
                        default=["hw1", "hw2", "hw3"])
    parser.add_argument("--group", choices=("main", "extra", "all"), default="all")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    cases = []
    summaries = []
    failed = False
    print(f"{'HW':<6} {'Group':<8} {'Passed':>7} {'Failed':>7} {'Total':>7}", flush=True)
    for hw in dict.fromkeys(args.hw):
        for group in (["main", "extra"] if args.group == "all" else [args.group]):
            paths = dataset_paths(group, ROOT / "tests" / hw)
            if not paths:
                print(f"{hw:<6} {group:<8} MISSING", flush=True)
                summaries.append({"hw": hw, "group": group, "missing": True})
                failed = True
                continue
            results = []
            for path in paths:
                try:
                    case = check_case(path)
                except OSError as error:
                    case = {"name": path.stem, "passed": False,
                            "expected": [], "codes": [], "exit_code": None,
                            "stderr": str(error)}
                case["hw"] = hw
                results.append(case)
                if args.verbose and not case["passed"]:
                    print(f"{hw}/{path.stem}: expected {case['expected'] or ['OK']}; "
                          f"actual {case['codes'] or [case['stderr'].strip() or 'OK']}",
                          flush=True)
            passed = sum(case["passed"] for case in results)
            total = len(results)
            print(f"{hw:<6} {group:<8} {passed:>7} {total - passed:>7} {total:>7}", flush=True)
            summaries.append({"hw": hw, "group": group, "passed": passed,
                              "failed": total - passed, "total": total})
            cases.extend(results)
            failed |= passed != total
    passed = sum(case["passed"] for case in cases)
    print(f"Total: {passed}/{len(cases)} passed")
    if args.report:
        args.report.write_text(json.dumps({"summary": summaries, "cases": cases},
                                         ensure_ascii=False, indent=2) + "\n")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
