from typing import Protocol, overload
from .integer import Integer
from .boolean import Boolean


class TimeDelta(Protocol):
    
    def __add__(self, other: "TimeDelta") -> "TimeDelta":
        ...

    def __sub__(self, other: "TimeDelta") -> "TimeDelta":
        ...

    def __mul__(self, other: Integer) -> "TimeDelta":
        ...

    @overload
    def __truediv__(self, other: Integer) -> "TimeDelta":
        ...

    @overload
    def __truediv__(self, other: "TimeDelta") -> Integer:
        ...

    @overload
    def __floordiv__(self, other: Integer) -> "TimeDelta":
        ...

    @overload
    def __floordiv__(self, other: "TimeDelta") -> Integer:
        ...

    def __mod__(self, other: "TimeDelta") -> "TimeDelta":
        ...

    def round(self, other: "TimeDelta") -> "TimeDelta":
        # NOTE: we don't use the __round__ method
        # because this expects an `ndigit` argument
        # which doesn't make sense for a timedelta.
        ...

    def floor(self, other: "TimeDelta") -> "TimeDelta":
        # NOTE: we don't use the __floor__ method
        # because this expects an `ndigit` argument
        # which doesn't make sense for a timedelta.
        ...

    def ceil(self, other: "TimeDelta") -> "TimeDelta":
        # NOTE: we don't use the __ceil__ method
        # because this expects an `ndigit` argument
        # which doesn't make sense for a timedelta.
        ...

    def __le__(self, other: "TimeDelta") -> Boolean:
        ...

    def __lt__(self, other: "TimeDelta") -> Boolean:
        ...

    def __ge__(self, other: "TimeDelta") -> Boolean:
        ...

    def __gt__(self, other: "TimeDelta") -> Boolean:
        ...

    def __eq__(self, other: "TimeDelta") -> Boolean:
        ...

    def __ne__(self, other: "TimeDelta") -> Boolean:
        ...