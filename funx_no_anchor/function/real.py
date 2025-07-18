from numbers import Real
from funx.function.elements.base import DataFunction
import polars as pl

class RealFunction(DataFunction):

    def __add__(self, other: float | int) -> 'RealFunction':
        if isinstance(other, (int, float)):
            added_pl_expr = (pl.col(self.schema.name) + other)

            new_pl_df = self.pl_df.with_columns(added_pl_expr.alias(self.schema.name))

            return RealFunction(new_pl_df, self.schema)
        raise TypeError