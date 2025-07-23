from .base import Base
from .. import data_types as dt


class Integer(Base, dtype=dt.IntegerType):

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__

    def __add__(self, other):
        match other.dtype:
            case dt.IntegerType() | dt.RealType():
                return self.from_polars(self.pl_expr + other.pl_expr, other.dtype)
            case _:
                return NotImplemented

    def __sub__(self, other):
        match other.dtype:
            case dt.IntegerType() | dt.RealType():
                return self.from_polars(self.pl_expr - other.pl_expr, other.dtype)
            case _:
                return NotImplemented

    def __mul__(self, other):
        match other.dtype:
            case dt.IntegerType() | dt.RealType():
                return self.from_polars(self.pl_expr * other.pl_expr, other.dtype)
            case _:
                return NotImplemented

    def __truediv__(self, other):
        match other.dtype:
            case dt.IntegerType() | dt.RealType():
                return self.from_polars(self.pl_expr / other.pl_expr, dt.RealType())
            case _:
                return NotImplemented

    def __floordiv__(self, other):
        match other.dtype:
            case dt.IntegerType() | dt.RealType():
                return self.from_polars(self.pl_expr // other.pl_expr, dt.IntegerType())
            case _:
                return NotImplemented