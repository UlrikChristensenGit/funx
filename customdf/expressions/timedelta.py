from .base import Base
from .integer import Integer
from .real import Real

class Timedelta(Base):

    @register_add
    def _(self, other):
        return [
            (Timedelta, Timedelta, self + other),
        ]

    @register_sub
    def _(self, other):
        return [
            (Timedelta, Timedelta, self - other),
        ]

    @register_mul
    def _(self, other):
        return [
            (Integer | Real, Timedelta, self * other),
        ]

    @register_div
    def _(self, other):
        return [
            (Integer | Real, Timedelta, self / other),
            (Timedelta, Real, self / other),
        ]
