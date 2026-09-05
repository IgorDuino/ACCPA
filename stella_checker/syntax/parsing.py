from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from .generated.stellaLexer import stellaLexer
from .generated.stellaParser import stellaParser


class ParseError(Exception):
    pass


class _StopOnFirstError(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseError(f"{line}:{column + 1}: {msg}")


def parse_program(source: str) -> stellaParser.ProgramContext:
    lexer = stellaLexer(InputStream(source))
    listener = _StopOnFirstError()
    lexer.removeErrorListeners()
    lexer.addErrorListener(listener)
    parser = stellaParser(CommonTokenStream(lexer))
    parser.removeErrorListeners()
    parser.addErrorListener(listener)

    return parser.start_Program().x
