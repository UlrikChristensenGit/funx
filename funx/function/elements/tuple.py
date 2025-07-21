from .base import DataFunction
from .data_types import TupleType, Field
from . import utils

import polars as pl

class TupleFunction(DataFunction):

    def __getitem__(self, key: str) -> 'Element':
        dtype = self.dtype.get(key)
        expr = self.expr.struct.field(key).alias(key)
        return utils.make_function(self.df, self.dims, dtype, expr)

    def elements(self) -> list[DataFunction]:
        return [self[field.name] for field in self.dtype.fields]

    @classmethod
    def from_elements(cls, mapping: dict[str, DataFunction] | list[DataFunction]) -> 'TupleFunction':
        if isinstance(mapping, list):
            mapping = {elem.name: elem for elem in mapping}

        if len(set([elem._anchor_id() for elem in mapping.values()])) > 1:
            raise ValueError("Can only combine functions coming from the same anchor. I.e. no broadcasting is allowed.")

        df = mapping[next(iter(mapping))].df
        dims = mapping[next(iter(mapping))].dims
        dtype = TupleType({k: v.dtype for k, v in mapping.items()})
        expr = pl.struct([v.expr.alias(k) for k, v in mapping.items()]).alias("tuple")

        return utils.make_function(df, dims, dtype, expr)

    def __add__(self, other):
        added_elements = [elem + other for elem in self.elements()]
        return self.from_elements(added_elements, name=self.schema.name)