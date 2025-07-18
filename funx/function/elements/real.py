from numbers import Real
from funx.function.elements.base import DataFunction
import polars as pl

class RealFunction(DataFunction):

    def __add__(self, other: float | int) -> 'RealFunction':
        if isinstance(other, (int, float)):
            var_expr = (self.var_expr + pl.lit(other))
        elif isinstance(other, RealFunction):
            if self._anchor_id() == other._anchor_id():
                var_expr=(self.var_expr + other.var_expr)
            else:
                raise ValueError("Can only add functions coming from the same anchor. I.e. no broadcasting is allowed.")
        else:
            raise TypeError(f"Unsupported type for addition: {type(other)}")

        return RealFunction(self.pl_df, self.schema, var_expr)