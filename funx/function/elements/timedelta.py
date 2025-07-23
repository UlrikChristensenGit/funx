from .base import DataFunction
from .integer import IntFunction
from .real import RealFunction

class TimedeltaFunction(DataFunction):

    @register_add
    def _(self, other):
        return [
            (TimedeltaFunction, TimedeltaFunction, self + other),
        ]

    @register_sub
    def _(self, other):
        return [
            (TimedeltaFunction, TimedeltaFunction, self - other),
        ]

    @register_mul
    def _(self, other):
        return [
            (IntFunction | RealFunction, TimedeltaFunction, self * other),
        ]

    @register_div
    def _(self, other):
        return [
            (IntFunction | RealFunction, TimedeltaFunction, self / other),
            (TimedeltaFunction, RealFunction, self / other),
        ]
