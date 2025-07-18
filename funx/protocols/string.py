from typing import Protocol
from .boolean import Boolean
from .integer import Integer


class String(Protocol):
    """
    Protocol for an abstract string.
    Based on the built-in `str` type in Python.
    """

    def capitalize(self) -> "String":
        ...

    def endswith(self, suffix: "String") -> Boolean:
        ...

    def startswith(self, prefix: "String") -> Boolean:
        ...

    def format(self, *args, **kwargs) -> "String":
        ...

    def lower(self) -> "String":
        ...

    def upper(self) -> "String":
        ...

    def __add__(self, other: "String") -> "String":
        ...

    def __eq__(self, other: "String") -> Boolean:
        ...

    def __ne__(self, other: "String") -> Boolean:
        ...

    def len(self) -> Integer:
        ...
