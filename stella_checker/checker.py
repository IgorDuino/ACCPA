from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import NoReturn, cast

from antlr4 import ParserRuleContext

from .errors import TypeCheckError, UnsupportedFeature
from .syntax.generated.stellaParser import stellaParser as P
from .types import (
    BOOL,
    NAT,
    UNIT,
    FunType,
    ListType,
    RecordType,
    RefType,
    SumType,
    TupleType,
    Type,
    VariantType,
    format_type,
)


class Context(dict[str, Type]):
    def __init__(self, variables: Mapping[str, Type] | Iterable[tuple[str, Type]] = (),
                 exception_type: Type | None = None) -> None:
        super().__init__(variables)
        self.exception_type: Type | None = exception_type

    def copy(self) -> Context:
        return Context(self, self.exception_type)
        # копирование неглубокое. возможно при переприсвоение в локальном контексте чегото внутри ссылочного типа можно сломаться
        

def fail(code: str, message: str, node: ParserRuleContext) -> NoReturn:
    raise TypeCheckError(code, message, node)


def require_equal(expected: Type, actual: Type, node: ParserRuleContext) -> None:

    if expected == actual:
        return
    if isinstance(expected, VariantType) and isinstance(actual, VariantType):
        missing = expected.fields.keys() - actual.fields.keys()
        if missing:
            fail("ERROR_MISSING_VARIANT_LABELS",
                 f"Missing variant labels: {', '.join(sorted(missing))}; "
                 f"expected {format_type(expected)}, found {format_type(actual)}", node)
    fail("ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION",
         f"Expected {format_type(expected)}, found {format_type(actual)}", node)


def read_type(node: P.StellatypeContext) -> Type:
    if isinstance(node, P.TypeParensContext):
        return read_type(node.type_)
    if isinstance(node, P.TypeNatContext):
        return NAT
    if isinstance(node, P.TypeBoolContext):
        return BOOL
    if isinstance(node, P.TypeUnitContext):
        return UNIT
    if isinstance(node, P.TypeFunContext):
        return FunType(tuple(read_type(t) for t in node.paramTypes), read_type(node.returnType))
    if isinstance(node, P.TypeTupleContext):
        return TupleType(tuple(read_type(t) for t in node.types))
    if isinstance(node, P.TypeSumContext):
        return SumType(read_type(node.left), read_type(node.right))
    if isinstance(node, P.TypeListContext):
        return ListType(read_type(node.types[0]))
    if isinstance(node, P.TypeRefContext):
        return RefType(read_type(node.type_))
    if isinstance(node, (P.TypeRecordContext, P.TypeVariantContext)):
        is_record = isinstance(node, P.TypeRecordContext)
        fields: dict[str, Type] = {}
        field: P.RecordFieldTypeContext | P.VariantFieldTypeContext
        for field in node.fieldTypes:
            name = field.label.text
            if name in fields:
                code = ("ERROR_DUPLICATE_RECORD_TYPE_FIELDS" if is_record
                        else "ERROR_DUPLICATE_VARIANT_TYPE_FIELDS")
                fail(code, f"Duplicate field {name} in type", field)
            if field.type_ is None:
                raise UnsupportedFeature("Variant labels without data are optional, not implemented")
            fields[name] = read_type(field.type_)
        return RecordType(fields) if is_record else VariantType(fields)
    raise UnsupportedFeature(f"Type {node.getText()} is not supported")


def function_signature(decl: P.DeclFunContext) -> FunType:
    if decl.returnType is None:
        raise UnsupportedFeature("Function result annotations are required in this checker")
    if decl.throwTypes:
        raise UnsupportedFeature("Function throws annotations are not supported")
    params = tuple(read_type(p.paramType) for p in decl.paramDecls)
    return FunType(params, read_type(decl.returnType))


def check_main(context: Context, node: P.ProgramContext) -> None:
    if "main" not in context:
        fail("ERROR_MISSING_MAIN", "No top-level main function", node)
    main_type = context["main"]
    if not isinstance(main_type, FunType):
        fail("ERROR_INCORRECT_TYPE_OF_MAIN", "main must have a function type", node)
    if len(main_type.parameters) != 1:
        fail("ERROR_INCORRECT_ARITY_OF_MAIN", "main must have exactly one parameter", node)


def collect_functions(declarations: Iterable[P.DeclContext], context: Context,
                      top_level: bool = False) -> list[tuple[P.DeclFunContext, FunType]]:
    signatures: list[tuple[P.DeclFunContext, FunType]] = []
    names: set[str] = set()
    for decl in declarations:
        if isinstance(decl, P.DeclExceptionTypeContext):
            if not top_level:
                fail("ERROR_ILLEGAL_LOCAL_EXCEPTION_TYPE", "Exception type must be declared at top level", decl)
            if context.exception_type is not None:
                fail("ERROR_DUPLICATE_EXCEPTION_TYPE", "Exception type is already declared", decl)
            context.exception_type = read_type(decl.exceptionType)
            continue
        if not isinstance(decl, P.DeclFunContext):
            raise UnsupportedFeature("Only ordinary function declarations are supported")
        name = decl.name.text
        if name in names:
            raise UnsupportedFeature(f"Duplicate function declaration: {name}")
        names.add(name)
        try:
            signature = function_signature(decl)
        except TypeCheckError as error:
            error.function = name
            raise
        context[name] = signature
        signatures.append((decl, signature))
    return signatures


def check_function(decl: P.DeclFunContext, signature: FunType, context: Context) -> None:
    local = context.copy()
    param: P.ParamDeclContext
    for param, type_ in zip(decl.paramDecls, signature.parameters):
        local[param.name.text] = type_
    try:
        for nested, nested_type in collect_functions(decl.localDecls, local):
            check_function(nested, nested_type, local)
        check(decl.returnExpr, signature.result, local)
    except TypeCheckError as error:
        if error.function is None:
            error.function = decl.name.text
        raise


def check_program(program: P.ProgramContext) -> None:
    context = Context()
    # print('Context before collected functions', context)
    functions = collect_functions(program.decls, context, top_level=True)
    # print('Context after collected functions', context)
    check_main(context, program)
    for decl, signature in functions:
        check_function(decl, signature, context)


def unwrap(node: P.ExprContext) -> P.ExprContext:
    while isinstance(node, P.ParenthesisedExprContext) or (
        isinstance(node, P.SequenceContext) and node.expr2 is None
    ):
        node = node.expr_ if isinstance(node, P.ParenthesisedExprContext) else node.expr1
    return node


def infer(node: P.ExprContext, context: Context) -> Type:
    node = unwrap(node)
    if isinstance(node, P.VarContext):
        name = node.name.text
        if name not in context:
            fail("ERROR_UNDEFINED_VARIABLE", f"Variable {name} is not defined", node)
        return context[name]
    if isinstance(node, (P.ConstTrueContext, P.ConstFalseContext)):
        return BOOL
    if isinstance(node, P.ConstIntContext):
        if node.sign is not None:
            fail("ERROR_ILLEGAL_NEGATIVE_LITERAL", "A Nat literal cannot be negative", node)
        return NAT
    if isinstance(node, P.ConstUnitContext):
        return UNIT
    if isinstance(node, P.PanicContext):
        fail("ERROR_AMBIGUOUS_PANIC_TYPE", "Panic needs an expected result type", node)
    if isinstance(node, P.ThrowContext):
        check(node.expr_, exception_type(context, node), context)
        fail("ERROR_AMBIGUOUS_THROW_TYPE", "Throw needs an expected result type", node)
    if isinstance(node, P.TryWithContext):
        result = infer(node.tryExpr, context)
        check(node.fallbackExpr, result, context)
        return result
    if isinstance(node, P.TryCatchContext):
        result = infer(node.tryExpr, context)
        check(node.fallbackExpr, result, catch_context(node, context))
        return result
    if isinstance(node, P.SequenceContext):
        check(node.expr1, UNIT, context)
        return infer(node.expr2, context)
    if isinstance(node, P.RefContext):
        return RefType(infer(node.expr_, context))
    if isinstance(node, P.ConstMemoryContext):
        fail("ERROR_AMBIGUOUS_REFERENCE_TYPE", "A memory address needs an expected reference type", node)
    if isinstance(node, P.DerefContext):
        return reference_type(node.expr_, context).element
    if isinstance(node, P.AssignContext):
        target = reference_type(node.lhs, context)
        check(node.rhs, target.element, context)
        return UNIT
    if isinstance(node, (P.SuccContext, P.PredContext, P.IsZeroContext)):
        check(node.n, NAT, context)
        return BOOL if isinstance(node, P.IsZeroContext) else NAT
    if isinstance(node, P.IfContext):
        check(node.condition, BOOL, context)
        result = infer(node.thenExpr, context)
        check(node.elseExpr, result, context)
        return result
    if isinstance(node, P.AbstractionContext):
        local = context.copy()
        parameters: list[Type] = []
        param: P.ParamDeclContext
        for param in node.paramDecls:
            type_ = read_type(param.paramType)
            parameters.append(type_)
            local[param.name.text] = type_
        return FunType(tuple(parameters), infer(node.returnExpr, local))
    if isinstance(node, P.ApplicationContext):
        function = infer(node.fun, context)
        if not isinstance(function, FunType):
            fail("ERROR_NOT_A_FUNCTION",
                 f"Cannot apply an expression of type {format_type(function)}", node.fun)
        if len(function.parameters) != len(node.args):
            fail("ERROR_INCORRECT_NUMBER_OF_ARGUMENTS",
                 f"Expected {len(function.parameters)} arguments, found {len(node.args)}", node)
        for arg, expected in zip(node.args, function.parameters):
            # function.parameters преобразованные типы
            # node.args ноды до инфр типа
            check(arg, expected, context)
        return function.result
    if isinstance(node, P.NatRecContext):
        check(node.n, NAT, context)
        result = infer(node.initial, context)
        check(node.step, FunType((NAT,), FunType((result,), result)), context)
        return result
    if isinstance(node, P.FixContext):
        operand = unwrap(node.expr_)
        if isinstance(operand, P.AbstractionContext) and len(operand.paramDecls) == 1:
            result = read_type(operand.paramDecls[0].paramType)
            check(operand, FunType((result,), result), context)
            return result
        function = infer(node.expr_, context)
        if not isinstance(function, FunType):
            fail("ERROR_NOT_A_FUNCTION", "fix expects a function", node.expr_)
        if len(function.parameters) != 1:
            fail("ERROR_INCORRECT_NUMBER_OF_ARGUMENTS", "fix expects a unary function", node)
        require_equal(function.parameters[0], function.result, node.expr_)
        return function.result
    if isinstance(node, P.TupleContext):
        return TupleType(tuple(infer(e, context) for e in node.exprs))
    if isinstance(node, P.DotTupleContext):
        type_ = infer(node.expr_, context)
        if not isinstance(type_, TupleType):
            fail("ERROR_NOT_A_TUPLE", f"Cannot project from {format_type(type_)}", node.expr_)
        index = int(node.index.text)
        if index < 1 or index > len(type_.items):
            fail("ERROR_TUPLE_INDEX_OUT_OF_BOUNDS",
                 f"Index {index} is outside 1..{len(type_.items)}", node)
        return type_.items[index - 1]
    if isinstance(node, P.RecordContext):
        bindings = record_bindings(node)
        return RecordType({name: infer(value, context) for name, value in bindings.items()})
    if isinstance(node, P.DotRecordContext):
        type_ = infer(node.expr_, context)
        if not isinstance(type_, RecordType):
            fail("ERROR_NOT_A_RECORD", f"Cannot access a field of {format_type(type_)}", node.expr_)
        name = node.label.text
        if name not in type_.fields:
            fail("ERROR_UNEXPECTED_FIELD_ACCESS", f"Record has no field {name}", node)
        return type_.fields[name]
    if isinstance(node, P.LetContext):
        return infer(node.body, let_context(node, context))
    if isinstance(node, P.TypeAscContext):
        type_ = read_type(node.type_)
        check(node.expr_, type_, context)
        return type_
    if isinstance(node, (P.InlContext, P.InrContext)):
        fail("ERROR_AMBIGUOUS_SUM_TYPE", "An injection needs an expected sum type or ascription", node)
    if isinstance(node, P.VariantContext):
        fail("ERROR_AMBIGUOUS_VARIANT_TYPE", "A variant needs an expected type or ascription", node)
    if isinstance(node, P.ListContext):
        if not node.exprs:
            fail("ERROR_AMBIGUOUS_LIST_TYPE", "An empty list needs an expected type or ascription", node)
        element = infer(node.exprs[0], context)
        for expr in node.exprs[1:]:
            check(expr, element, context)
        return ListType(element)
    if isinstance(node, P.ConsListContext):
        element = infer(node.head, context)
        check(node.tail, ListType(element), context)
        return ListType(element)
    if isinstance(node, (P.HeadContext, P.TailContext, P.IsEmptyContext)):
        type_ = infer(node.list_, context)
        if not isinstance(type_, ListType):
            fail("ERROR_NOT_A_LIST", f"Expected a list, found {format_type(type_)}", node.list_)
        if isinstance(node, P.HeadContext):
            return type_.element
        return BOOL if isinstance(node, P.IsEmptyContext) else type_
    if isinstance(node, P.MatchContext):
        return match_type(node, context)
    raise UnsupportedFeature(f"Expression {type(node).__name__} is not supported")


def check(node: P.ExprContext, expected: Type, context: Context) -> None:
    node = unwrap(node)
    if isinstance(node, P.PanicContext):
        return
    if isinstance(node, P.ThrowContext):
        check(node.expr_, exception_type(context, node), context)
        return
    if isinstance(node, P.TryWithContext):
        check(node.tryExpr, expected, context)
        check(node.fallbackExpr, expected, context)
        return
    if isinstance(node, P.TryCatchContext):
        check(node.tryExpr, expected, context)
        check(node.fallbackExpr, expected, catch_context(node, context))
        return
    if isinstance(node, P.SequenceContext):
        check(node.expr1, UNIT, context)
        check(node.expr2, expected, context)
        return
    if isinstance(node, P.RefContext):
        if not isinstance(expected, RefType):
            fail("ERROR_UNEXPECTED_REFERENCE", f"Expected {format_type(expected)}, found a reference", node)
        check(node.expr_, expected.element, context)
        return
    if isinstance(node, P.ConstMemoryContext):
        if not isinstance(expected, RefType):
            fail("ERROR_UNEXPECTED_MEMORY_ADDRESS", f"Expected {format_type(expected)}, found a memory address", node)
        return
    if isinstance(node, P.DerefContext):
        try:
            check(node.expr_, RefType(expected), context)
        except TypeCheckError as error:
            if error.code != "ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION":
                raise
            try:
                actual = infer(node.expr_, context)
            except (TypeCheckError, UnsupportedFeature):
                raise error
            if not isinstance(actual, RefType):
                fail("ERROR_NOT_A_REFERENCE", f"Expected a reference, found {format_type(actual)}", node.expr_)
            raise
        return
    if isinstance(node, P.AbstractionContext):
        if not isinstance(expected, FunType):
            fail("ERROR_UNEXPECTED_LAMBDA", f"Expected {format_type(expected)}, found a lambda", node)
        if len(node.paramDecls) != len(expected.parameters):
            fail("ERROR_UNEXPECTED_NUMBER_OF_PARAMETERS_IN_LAMBDA",
                 f"Expected {len(expected.parameters)} parameters, found {len(node.paramDecls)}", node)
        local = context.copy()
        for param, type_ in zip(node.paramDecls, expected.parameters):
            actual = read_type(param.paramType)
            if actual != type_:
                fail("ERROR_UNEXPECTED_TYPE_FOR_PARAMETER",
                     f"Expected parameter type {format_type(type_)}, found {format_type(actual)}", param)
            local[param.name.text] = actual
        check(node.returnExpr, expected.result, local)
        return
    if isinstance(node, P.IfContext):
        check(node.condition, BOOL, context)
        check(node.thenExpr, expected, context)
        check(node.elseExpr, expected, context)
        return
    if isinstance(node, P.NatRecContext):
        check(node.n, NAT, context)
        check(node.initial, expected, context)
        check(node.step, FunType((NAT,), FunType((expected,), expected)), context)
        return
    if isinstance(node, P.TupleContext):
        if not isinstance(expected, TupleType):
            fail("ERROR_UNEXPECTED_TUPLE", f"Expected {format_type(expected)}, found a tuple", node)
        if len(node.exprs) != len(expected.items):
            fail("ERROR_UNEXPECTED_TUPLE_LENGTH",
                 f"Expected {len(expected.items)} components, found {len(node.exprs)}", node)
        for expr, type_ in zip(node.exprs, expected.items):
            check(expr, type_, context)
        return
    if isinstance(node, P.RecordContext):
        if not isinstance(expected, RecordType):
            fail("ERROR_UNEXPECTED_RECORD", f"Expected {format_type(expected)}, found a record", node)
        bindings = record_bindings(node)
        missing = expected.fields.keys() - bindings.keys()
        extra = bindings.keys() - expected.fields.keys()
        if missing:
            fail("ERROR_MISSING_RECORD_FIELDS", f"Missing fields: {', '.join(sorted(missing))}", node)
        if extra:
            fail("ERROR_UNEXPECTED_RECORD_FIELDS", f"Unexpected fields: {', '.join(sorted(extra))}", node)
        for name, expr in bindings.items():
            check(expr, expected.fields[name], context)
        return
    if isinstance(node, (P.InlContext, P.InrContext)):
        if not isinstance(expected, SumType):
            fail("ERROR_UNEXPECTED_INJECTION", f"Expected {format_type(expected)}, found an injection", node)
        payload = expected.left if isinstance(node, P.InlContext) else expected.right
        check(node.expr_, payload, context)
        return
    if isinstance(node, P.VariantContext):
        if not isinstance(expected, VariantType):
            fail("ERROR_UNEXPECTED_VARIANT", f"Expected {format_type(expected)}, found a variant", node)
        name = node.label.text
        if name not in expected.fields:
            fail("ERROR_UNEXPECTED_VARIANT_LABEL", f"Variant type has no label {name}", node)
        if node.rhs is None:
            raise UnsupportedFeature("Variant labels without data are optional, not implemented")
        check(node.rhs, expected.fields[name], context)
        return
    if isinstance(node, (P.ListContext, P.ConsListContext)):
        if not isinstance(expected, ListType):
            fail("ERROR_UNEXPECTED_LIST", f"Expected {format_type(expected)}, found a list", node)
        if isinstance(node, P.ListContext):
            for expr in node.exprs:
                check(expr, expected.element, context)
        else:
            check(node.head, expected.element, context)
            check(node.tail, expected, context)
        return
    if isinstance(node, P.LetContext):
        check(node.body, expected, let_context(node, context))
        return
    if isinstance(node, P.MatchContext):
        match_type(node, context, expected)
        return
    if isinstance(node, P.HeadContext) and isinstance(unwrap(node.list_), (P.ListContext, P.ConsListContext)):

        check(node.list_, ListType(expected), context)
        return
    require_equal(expected, infer(node, context), node)


def reference_type(node: P.ExprContext, context: Context) -> RefType:
    type_ = infer(node, context)
    if not isinstance(type_, RefType):
        fail("ERROR_NOT_A_REFERENCE", f"Expected a reference, found {format_type(type_)}", node)
    return type_


def exception_type(context: Context, node: ParserRuleContext) -> Type:
    if context.exception_type is None:
        fail("ERROR_EXCEPTION_TYPE_NOT_DECLARED", "Declare an exception type", node)
    return context.exception_type


def catch_context(node: P.TryCatchContext, context: Context) -> Context:
    type_ = exception_type(context, node)
    local = context.copy()
    local.update(pattern_bindings(node.pat, type_, allow_literals=True))
    return local


def record_bindings(node: P.RecordContext) -> dict[str, P.ExprContext]:
    bindings: dict[str, P.ExprContext] = {}
    binding: P.BindingContext
    for binding in node.bindings:
        name = binding.name.text
        if name in bindings:
            fail("ERROR_DUPLICATE_RECORD_FIELDS", f"Duplicate record field {name}", binding)
        bindings[name] = binding.rhs
    return bindings


def let_context(node: P.LetContext, context: Context) -> Context:
    local = context.copy()
    binding: P.PatternBindingContext
    for binding in node.patternBindings:
        type_ = infer(binding.rhs, local)
        if not isinstance(binding.pat, P.PatternVarContext):
            raise UnsupportedFeature("Structural let patterns are optional, not implemented")
        local[binding.pat.name.text] = type_
    return local


def unwrap_pattern(pattern: P.PatternContext) -> P.PatternContext:
    while isinstance(pattern, P.ParenthesisedPatternContext):
        pattern = pattern.pattern_
    return pattern


def pattern_bindings(pattern: P.PatternContext, type_: Type,
                     allow_literals: bool = False) -> dict[str, Type]:
    pattern = unwrap_pattern(pattern)
    if isinstance(pattern, P.PatternVarContext):
        return {pattern.name.text: type_}
    if allow_literals:
        if isinstance(pattern, (P.PatternTrueContext, P.PatternFalseContext)) and type_ == BOOL:
            return {}
        if isinstance(pattern, P.PatternUnitContext) and type_ == UNIT:
            return {}
        if isinstance(pattern, P.PatternIntContext) and type_ == NAT:
            return {}
        if isinstance(pattern, P.PatternSuccContext) and type_ == NAT:
            return pattern_bindings(pattern.pattern_, NAT, allow_literals=True)
    if isinstance(pattern, (P.PatternInlContext, P.PatternInrContext)) and isinstance(type_, SumType):
        payload = type_.left if isinstance(pattern, P.PatternInlContext) else type_.right
        return pattern_bindings(pattern.pattern_, payload, allow_literals)
    if isinstance(pattern, P.PatternVariantContext) and isinstance(type_, VariantType):
        name = pattern.label.text
        if name in type_.fields and pattern.pattern_ is not None:
            return pattern_bindings(pattern.pattern_, type_.fields[name], allow_literals)
    fail("ERROR_UNEXPECTED_PATTERN_FOR_TYPE",
         f"Pattern does not match type {format_type(type_)}", pattern)


def exhaustive(patterns: Iterable[P.PatternContext], type_: Type) -> bool:
    patterns = [unwrap_pattern(p) for p in patterns]
    if any(isinstance(p, P.PatternVarContext) for p in patterns):
        return True
    if isinstance(type_, SumType):
        left = [p.pattern_ for p in patterns if isinstance(p, P.PatternInlContext)]
        right = [p.pattern_ for p in patterns if isinstance(p, P.PatternInrContext)]
        return exhaustive(left, type_.left) and exhaustive(right, type_.right)
    if isinstance(type_, VariantType):
        for name, payload in type_.fields.items():
            children = [p.pattern_ for p in patterns
                        if isinstance(p, P.PatternVariantContext) and p.label.text == name]
            if not exhaustive(children, payload):
                return False
        return True
    return False


def match_type(node: P.MatchContext, context: Context, expected: Type | None = None) -> Type:
    if not node.cases:
        fail("ERROR_ILLEGAL_EMPTY_MATCHING", "A match must contain at least one branch", node)
    scrutinized = infer(node.expr(), context)
    result = expected
    case: P.MatchCaseContext
    for case in node.cases:
        local = context.copy()
        local.update(pattern_bindings(case.pattern_, scrutinized))
        if result is None:
            result = infer(case.expr_, local)
        else:
            check(case.expr_, result, local)
    if not exhaustive([case.pattern_ for case in node.cases], scrutinized):
        fail("ERROR_NONEXHAUSTIVE_MATCH_PATTERNS",
             f"Patterns do not cover all cases of {format_type(scrutinized)}", node)
    return cast(Type, result)
