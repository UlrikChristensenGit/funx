from typing import Protocol


class Boolean(Protocol):
    """
    Protocol for an abstract boolean value.
    Based on the built-in `bool` type in Python.
    """

    def __and__(self, other: "Boolean") -> "Boolean":
        ...

    def __or__(self, other: "Boolean") -> "Boolean":
        ...

    def __xor__(self, other: "Boolean") -> "Boolean":
        ...

    def __invert__(self) -> "Boolean":
        ...
