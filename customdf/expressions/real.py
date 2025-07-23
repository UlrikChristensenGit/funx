from .base import Base
from .. import data_types as dt


class Real(Base, dtype=dt.RealType):

    def __mul__(self, other):
        match other.dtype:
            case dt.IntegerType() | dt.RealType():
                return self.from_polars(self.pl_expr * other.pl_expr, dt.RealType())
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
                return self.from_polars(self.pl_expr // other.pl_expr, dt.RealType())
            case _:
                return NotImplemented


        