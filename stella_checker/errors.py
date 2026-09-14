from antlr4 import ParserRuleContext


class TypeCheckError(Exception):
    def __init__(self, code: str, message: str, node: ParserRuleContext | None = None) -> None:
        self.code = code
        self.message = message
        self.function: str | None = None
        self.location: str | None = None
        self.expression: str | None = None
        if node is not None and node.start is not None:
            self.location = f"{node.start.line}:{node.start.column + 1}"
            if node.stop is not None:
                source = node.start.getInputStream().strdata
                self.expression = source[node.start.start:node.stop.stop + 1]
        super().__init__(message)

    def __str__(self) -> str:
        lines = [f"{self.code}: {self.message}"]
        if self.function is not None:
            lines.append(f"  in function {self.function}")
        if self.location is not None:
            lines.append(f"  at {self.location}")
        if self.expression is not None:
            text = " ".join(self.expression.split())
            lines.append(f"  expression: {text[:240]}")
        return "\n".join(lines)


class UnsupportedFeature(Exception):
    pass
