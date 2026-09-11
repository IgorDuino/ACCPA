from .errors import TypeCheckError, UnsupportedFeature
from .syntax.generated.stellaParser import stellaParser as P
from .types import (
    BOOL, NAT, UNIT, FunType, ListType, RecordType, RefType, SumType, TupleType,
    Type, VariantType, format_type,
)


def fail(code, message, node):
    raise TypeCheckError(code, message, node)


def require_equal(expected, actual, node):

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


def read_type(node) -> Type:
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
        fields = {}
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
    raise UnsupportedFeature(f"Type {node.getText()} is outside Stage 1")


def function_signature(decl):
    if decl.returnType is None:
        raise UnsupportedFeature("Function result annotations are required in this checker")
    if decl.throwTypes:
        raise UnsupportedFeature("Exception declarations belong to Stage 2")
    params = tuple(read_type(p.paramType) for p in decl.paramDecls)
    return FunType(params, read_type(decl.returnType))


def check_main(context, node):
    if "main" not in context:
        fail("ERROR_MISSING_MAIN", "No top-level main function", node)
    if not isinstance(context["main"], FunType):
        fail("ERROR_INCORRECT_TYPE_OF_MAIN", "main must have a function type", node)
    if len(context["main"].parameters) != 1:
        fail("ERROR_INCORRECT_ARITY_OF_MAIN", "main must have exactly one parameter", node)


def collect_functions(declarations, context):
    signatures = []
    names = set()
    for decl in declarations:
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
        signatures.append(signature)
    return signatures


def check_function(decl, signature, context):
    local = context.copy()
    for param, type_ in zip(decl.paramDecls, signature.parameters):
        local[param.name.text] = type_
    nested_types = collect_functions(decl.localDecls, local)
    for nested, nested_type in zip(decl.localDecls, nested_types):
        check_function(nested, nested_type, local)
    try:
        check(decl.returnExpr, signature.result, local)
    except TypeCheckError as error:
        error.function = decl.name.text
        raise


def check_program(program: P.ProgramContext) -> None:
    context = {}
    signatures = collect_functions(program.decls, context)
    check_main(context, program)
    for decl, signature in zip(program.decls, signatures):
        check_function(decl, signature, context)


def unwrap(node):

    while isinstance(node, P.ParenthesisedExprContext) or (
        isinstance(node, P.SequenceContext) and node.expr2 is None
    ):
        node = node.expr_ if isinstance(node, P.ParenthesisedExprContext) else node.expr1
    return node


def infer(node, context) -> Type:
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
    if isinstance(node, P.TryWithContext):
        result = infer(node.tryExpr, context)
        check(node.fallbackExpr, result, context)
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
        parameters = []
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
    raise UnsupportedFeature(f"Expression {type(node).__name__} is outside Stage 1")


def check(node, expected: Type, context) -> None:
    node = unwrap(node)
    if isinstance(node, P.PanicContext):
        return
    if isinstance(node, P.TryWithContext):
        check(node.tryExpr, expected, context)
        check(node.fallbackExpr, expected, context)
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
            actual = reference_type(node.expr_, context)
        except TypeCheckError as error:
            if error.code not in {
                "ERROR_AMBIGUOUS_REFERENCE_TYPE", "ERROR_AMBIGUOUS_LIST_TYPE",
                "ERROR_AMBIGUOUS_SUM_TYPE", "ERROR_AMBIGUOUS_VARIANT_TYPE",
                "ERROR_AMBIGUOUS_PANIC_TYPE", "ERROR_AMBIGUOUS_THROW_TYPE",
            }:
                raise
            check(node.expr_, RefType(expected), context)
            return
        require_equal(expected, actual.element, node)
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


def reference_type(node, context):
    type_ = infer(node, context)
    if not isinstance(type_, RefType):
        fail("ERROR_NOT_A_REFERENCE", f"Expected a reference, found {format_type(type_)}", node)
    return type_


def record_bindings(node):
    bindings = {}
    for binding in node.bindings:
        name = binding.name.text
        if name in bindings:
            fail("ERROR_DUPLICATE_RECORD_FIELDS", f"Duplicate record field {name}", binding)
        bindings[name] = binding.rhs
    return bindings


def let_context(node, context):
    local = context.copy()
    for binding in node.patternBindings:

        type_ = infer(binding.rhs, local)
        if not isinstance(binding.pat, P.PatternVarContext):
            raise UnsupportedFeature("Structural let patterns are optional, not implemented")
        local[binding.pat.name.text] = type_
    return local


def unwrap_pattern(pattern):
    while isinstance(pattern, P.ParenthesisedPatternContext):
        pattern = pattern.pattern_
    return pattern


def pattern_bindings(pattern, type_):
    pattern = unwrap_pattern(pattern)
    if isinstance(pattern, P.PatternVarContext):
        return {pattern.name.text: type_}
    if isinstance(pattern, (P.PatternInlContext, P.PatternInrContext)):
        if isinstance(type_, SumType):
            payload = type_.left if isinstance(pattern, P.PatternInlContext) else type_.right
            return pattern_bindings(pattern.pattern_, payload)
    if isinstance(pattern, P.PatternVariantContext) and isinstance(type_, VariantType):
        name = pattern.label.text
        if name in type_.fields and pattern.pattern_ is not None:
            return pattern_bindings(pattern.pattern_, type_.fields[name])
    fail("ERROR_UNEXPECTED_PATTERN_FOR_TYPE",
         f"Pattern does not match type {format_type(type_)}", pattern)


def exhaustive(patterns, type_):
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


def match_type(node, context, expected=None):
    if not node.cases:
        fail("ERROR_ILLEGAL_EMPTY_MATCHING", "A match must contain at least one branch", node)
    scrutinized = infer(node.expr(), context)
    result = expected
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
    return result
