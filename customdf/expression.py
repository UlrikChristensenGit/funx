import polars as pl
from .data_types import DataType

class Expression:

    def __init__(self, pl_expr: pl.Expr, dtype: DataType):
        self.pl_expr = pl_expr
        self.dtype = dtype

    def __repr__(self):
        return f"Expression({self.pl_expr}, {self.dtype})"