from typing import Protocol, overload
from .timedelta import TimeDelta
from .boolean import Boolean


class Timestamp(Protocol):

    @overload
    def __sub__(self, other: "Timestamp") -> TimeDelta:
        # subtracting two timestamps results in a timedelta
        # NOTE: this should probably be another method (e.g. `diff(t1, t2)`)
        # but it is standard to use the subtraction notation for this operation.
        ...

    @overload
    def __sub__(self, other: TimeDelta) -> "Timestamp":
        # subtracting a timedelta from a timestamp results in a timestamp
        ...

    def __add__(self, other: TimeDelta) -> "Timestamp":
        ...

    def round(self, other: TimeDelta) -> "Timestamp":
        # NOTE: we don't use the __round__ method
        # because this expects an `ndigit` argument
        # which doesn't make sense for a timestamp.
        ...

    def floor(self, other: TimeDelta) -> "Timestamp":
        # NOTE: we don't use the __floor__ method
        # because this expects an `ndigit` argument
        # which doesn't make sense for a timestamp.
        ...

    def ceil(self, other: TimeDelta) -> "Timestamp":
        # NOTE: we don't use the __ceil__ method
        # because this expects an `ndigit` argument
        # which doesn't make sense for a timestamp.
        ...

    def __le__(self, other: "Timestamp") -> Boolean:
        ...

    def __lt__(self, other: "Timestamp") -> Boolean:
        ...

    def __ge__(self, other: "Timestamp") -> Boolean:
        ...

    def __gt__(self, other: "Timestamp") -> Boolean:
        ...

    def __eq__(self, other: "Timestamp") -> Boolean:
        ...

    def __ne__(self, other: "Timestamp") -> Boolean:
        ...
