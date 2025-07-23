from typing import Protocol
from .integer import Integer


class Real(Protocol):
    """
    Protocol for an abstract real number.
    Based on the built-in `float` type in Python.
    """

    def __add__(self, other: "Real" | Integer) -> "Real":
        ...

    def __sub__(self, other: "Real" | Integer) -> "Real":
        ...

    def __mul__(self, other: "Real" | Integer) -> "Real":
        ...

    def __truediv__(self, other: "Real" | Integer) -> "Real":
        ...

    def __floordiv__(self, other: "Real" | Integer) -> "Real":
        ...

    def __mod__(self, other: "Real" | Integer) -> "Real":
        ...

    def __pow__(self, other: "Real" | Integer) -> "Real":
        ...

    def __round__(self, ndigits: Integer = None) -> "Integer":
        ...

    def __trunc__(self) -> Integer:
        ...

    def __floor__(self) -> Integer:
        ...

    def __ceil__(self) -> Integer:
        ...
