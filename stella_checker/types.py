from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BaseType:
    name: str


@dataclass(frozen=True)
class FunType:
    parameters: tuple[Type, ...]
    result: Type


@dataclass(frozen=True)
class TupleType:
    items: tuple[Type, ...]


@dataclass(frozen=True)
class RecordType:
    fields: dict[str, Type]


@dataclass(frozen=True)
class SumType:
    left: Type
    right: Type


@dataclass(frozen=True)
class ListType:
    element: Type


@dataclass(frozen=True)
class RefType:
    element: Type


@dataclass(frozen=True)
class VariantType:
    fields: dict[str, Type]


Type = BaseType | FunType | TupleType | RecordType | SumType | ListType | RefType | VariantType
NAT = BaseType("Nat")
BOOL = BaseType("Bool")
UNIT = BaseType("Unit")


def format_type(type_: Type) -> str:
    if isinstance(type_, BaseType):
        return type_.name
    if isinstance(type_, FunType):
        args = ", ".join(format_type(t) for t in type_.parameters)
        return f"fn({args}) -> {format_type(type_.result)}"
    if isinstance(type_, TupleType):
        return "{" + ", ".join(format_type(t) for t in type_.items) + "}"
    if isinstance(type_, RecordType):
        fields = (f"{name}: {format_type(t)}" for name, t in type_.fields.items())
        return "{" + ", ".join(fields) + "}"
    if isinstance(type_, SumType):
        return f"({format_type(type_.left)} + {format_type(type_.right)})"
    if isinstance(type_, ListType):
        return f"[{format_type(type_.element)}]"
    if isinstance(type_, RefType):
        return f"&({format_type(type_.element)})"
    if isinstance(type_, VariantType):
        fields = (f"{name}: {format_type(t)}" for name, t in type_.fields.items())
        return "<| " + ", ".join(fields) + " |>"
    raise TypeError(f"Unknown internal type: {type_!r}")
