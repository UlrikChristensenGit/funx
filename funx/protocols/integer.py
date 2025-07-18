from typing import Protocol
from .real import Real


class Integer(Protocol):
    """
    Protocol for an abstract integer number.
    Based on the built-in `int` type in Python.
    """

    def __add__(self, other: "Integer") -> "Integer":
        ...

    def __sub__(self, other: "Integer") -> "Integer":
        ...

    def __mul__(self, other: "Integer") -> "Integer":
        ...

    def __floordiv__(self, other: "Integer") -> "Integer":
        ...

    def __truediv__(self, other: "Integer") -> Real:
        ...

    def __mod__(self, other: "Integer") -> "Integer":
        ...

    def __pow__(self, other: "Integer" | Real) -> Real:
        ...

    def __round__(self, ndigits: "Integer" = None) -> "Integer":
        ...

    def __trunc__(self) -> "Integer":
        ...

    def __floor__(self) -> "Integer":
        ...

    def __ceil__(self) -> "Integer":
        ...
