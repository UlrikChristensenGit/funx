import polars as pl
from funx.function.schema import Schema
from funx.function.data_types import TupleType, RealType
import os

os.environ["POLARS_FMT_TABLE_HIDE_DATAFRAME_SHAPE_INFORMATION"] = "1"


class DataFunction:

    def __init__(
        self,
        pl_df: pl.DataFrame,
        schema: Schema
    ):
        self.pl_df = pl_df
        self.schema = schema


    def __repr__(self) -> str:
        return repr(self.schema)

    def _repr_html_(self) -> str:
        if isinstance(self.schema.dtype, TupleType):
            var_cols = pl.col(self.schema.name).struct.unnest()
        else:
            var_cols = pl.col(self.schema.name)

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