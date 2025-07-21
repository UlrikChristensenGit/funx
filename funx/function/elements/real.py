from .base import DataFunction
import polars as pl
from . import utils

class RealFunction(DataFunction):

    def __add__(self, other: float | int) -> 'RealFunction':
        if isinstance(other, (int, float)):
            expr = (self.expr + pl.lit(other))
        elif isinstance(other, RealFunction):
            if self._anchor_id() == other._anchor_id():
                expr=(self.expr + other.expr)
            else:
                raise ValueError("Can only add functions coming from the same anchor. I.e. no broadcasting is allowed.")
        else:
            raise TypeError(f"Unsupported type for addition: {type(other)}")

        return utils.make_function(
            self.df,
            self.dims,
            self.dtype,
            expr
        )
    
    def __add__(self, other: 'RealFunction') -> 'RealFunction':
        combined = combine(self, other)
        exprs = self.expr + other.expr
