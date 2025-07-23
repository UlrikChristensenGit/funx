from .base import DataFunction
from .timedelta import TimedeltaFunction

class TimestampFunction(DataFunction):

    @register_add
    def _(self, other):
        return [
            (TimedeltaFunction, TimestampFunction, self + other),
        ]

    @register_sub
    def _(self, other):
        return [
            (TimedeltaFunction, TimestampFunction, self - other),
            (TimestampFunction, TimedeltaFunction, self - other),
        ]
