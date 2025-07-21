import polars as pl
from funx.function.elements.schema import Schema
from funx.function.elements.data_types import TupleType, RealType
import os

os.environ["POLARS_FMT_TABLE_HIDE_DATAFRAME_SHAPE_INFORMATION"] = "1"


class DataFunction:

    def __init__(
        self,
        pl_df: pl.DataFrame,
        schema: Schema,
        var_expr: pl.Expr | None = None
    ):
        self.pl_df = pl_df
        self.schema = schema
        if var_expr is None:
            self.var_expr = pl.col(self.schema.name)
        else:
            self.var_expr = var_expr

    def _anchor_id(self) -> str:
        return f"{id(self.pl_df)}_{id(self.schema.dims)}"

    def __repr__(self) -> str:
        return repr(self.schema)

    def _repr_html_(self) -> str:
        if isinstance(self.schema.dtype, TupleType):
            var_cols = self.var_expr.struct.unnest()
        else:
            var_cols = self.var_expr

        return f"""<b>{self.schema.name}</b><br>
        <table>
            <tr>
                <th>Dimensions</th>
                <th>Variables</th>
            </tr>
            <tr>
                <td>{self.pl_df.select(self.schema.dims.keys())._repr_html_()}</td>
                <td>{self.pl_df.select(var_cols)._repr_html_()}</td>
            </tr>
        </table>
        """