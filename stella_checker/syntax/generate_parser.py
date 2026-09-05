# ANTLR 4.13.2 
# правила из https://github.com/IU-ACCPA-2023/stella-implementation-in-typescript/tree/de023f6048ca0e09ffe377bd60a1fdc3354b0317

import argparse
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("jar", type=Path, help="path to antlr-4.13.2-complete.jar")
args = parser.parse_args()
jar = args.jar.resolve(strict=True)
syntax = Path(__file__).resolve().parent
result = subprocess.run(["java", "-jar", str(jar)], capture_output=True, text=True, check=True)
if "Version 4.13.2" not in result.stdout:
    parser.error("Use ANTLR 4.13.2 to match the pinned Python runtime.")
subprocess.run([
    "java", "-jar", str(jar), "-Dlanguage=Python3", "-visitor", "-no-listener",
    "-o", "../generated", "stellaLexer.g4", "stellaParser.g4",
], cwd=syntax / "grammar", check=True)
