import polars as pl
from ..data_types import DataType
from typing_extensions import Self

class BaseExpr:

    registry = dict()

    def __init__(self, pl_expr: pl.Expr, dtype: DataType):
        self.pl_expr = pl_expr
        self.dtype = dtype

    def __init_subclass__(cls, dtype: type[DataType]):
        if dtype not in cls.registry:
            cls.registry[dtype] = cls

    def __repr__(self):
        return f"({self.pl_expr}, {self.dtype})"

    def alias(self, name: str) -> Self:
        pl_expr = self.pl_expr.alias(name)
        return self.__class__(pl_expr, self.dtype)
    
    @classmethod
    def from_polars(cls, pl_expr: pl.Expr, dtype: DataType) -> Self:
        subclass = cls.registry[dtype.__class__]
        return subclass(pl_expr, dtype)
