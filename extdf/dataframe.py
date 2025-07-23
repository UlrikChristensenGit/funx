import polars as pl
from .data_types import DataType
from .unresolved import UnresolvedExpr
from .expressions.base import BaseExpr


class DataFrame:

    def __init__(
        self,
        pl_df: pl.DataFrame,
        schema: dict[str, DataType],
    ):
        self.pl_df = pl_df
        self.schema = schema

    def __repr__(self):
        return repr(self.pl_df)

    def _repr_html_(self):
        return self.pl_df._repr_html_()

    def _resolve_column_name(self, name: str) -> BaseExpr:
        return BaseExpr.from_polars(pl.col(name), self.schema[name])

    def select(self, exprs: list[UnresolvedExpr]) -> 'DataFrame':
        exprs = [expr.resolve(self) for expr in exprs]
        schema = {expr.pl_expr.meta.output_name(): expr.dtype for expr in exprs}
        df = self.pl_df.select([expr.pl_expr for expr in exprs])
        return DataFrame(df, schema)

    def row(self, index: int) -> tuple:
        pl_row = self.pl_df.row(index, named=True)
        return {k: utils.pl_scalar_to_python(v, self.schema[k]) for k, v in pl_row.items()}
