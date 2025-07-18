from .base import DataFunction
from funx.function.schema import Schema
import polars as pl


class TupleFunction(DataFunction):

    def __getitem__(self, key: str) -> 'Element':
        element = self.schema.dtype.get(key)
        new_schema = Schema(
            dims=self.schema.dims,
            name=element.name,
            dtype=element.dtype
        )
        new_pl_df = self.pl_df.select(list(self.schema.dims.keys()) + [pl.col(self.schema.name).struct.field(key)])
        return DataFunction(new_pl_df, new_schema)
