from .base import DataFunction
from funx.function.elements.schema import Schema
from funx.function.elements.real import RealFunction
from funx.function.elements.data_types import RealType, TupleType, Field
import polars as pl

class TupleFunction(DataFunction):

    def __getitem__(self, key: str) -> 'Element':
        element = self.schema.dtype.get(key)
        new_schema = Schema(
            dims=self.schema.dims,
            name=element.name,
            dtype=element.dtype
        )
        new_var_expr = self.var_expr.struct.field(key)
        if isinstance(element.dtype, RealType):
            return RealFunction(self.pl_df, new_schema, new_var_expr)
        
    def elements(self) -> list[DataFunction]:
        return [self[field.name] for field in self.schema.dtype.fields]

    @classmethod
    def from_elements(cls, elements: list[DataFunction], name: str = "tuple") -> 'TupleFunction':
        if len(set([elem._anchor_id() for elem in elements])) > 1:
            raise ValueError("Can only combine functions coming from the same anchor. I.e. no broadcasting is allowed.")

        pl_df = elements[0].pl_df
        var_expr = pl.struct([elem.var_expr for elem in elements]).alias(name)
        dtype = TupleType([Field(elem.schema.name, elem.schema.dtype) for elem in elements])

        schema = Schema(
            dims=elements[0].schema.dims,
            name=name,
            dtype=dtype
        )

        return TupleFunction(pl_df, schema, var_expr)
    
    def __add__(self, other):
        added_elements = [elem + other for elem in self.elements()]
        return self.from_elements(added_elements, name=self.schema.name)