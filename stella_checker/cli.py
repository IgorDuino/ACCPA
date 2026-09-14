import argparse
from pathlib import Path
import sys

from .checker import check_program
from .errors import TypeCheckError, UnsupportedFeature
from .syntax.parsing import ParseError, parse_program
from .syntax.tree import format_tree


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Stella type checker")
    parser.add_argument("file", nargs="?", default="-")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--tree", action="store_true", help="print indented syntax tree with source positions")
    args = parser.parse_args(argv)

    try:
        source = sys.stdin.read() if args.file == "-" else Path(args.file).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"INPUT_ERROR: {exc}", file=sys.stderr)
        return 2

    try:
        program = parse_program(source)
    except ParseError as exc:
        print(f"SYNTAX_ERROR: {args.file}:{exc}", file=sys.stderr)
        return 2

    if args.tree:
        print(format_tree(program))
        return 0

    try:
        check_program(program)
    except TypeCheckError as exc:
        print(exc, file=sys.stderr)
        return 1
    except UnsupportedFeature as exc:
        print(f"UNSUPPORTED_FEATURE: {exc}", file=sys.stderr)
        return 3
    return 0
