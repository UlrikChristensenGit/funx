import polars as pl
from .data_types import DataType, TupleType, Field
from abc import ABC, abstractmethod
import os
from . import utils

os.environ["POLARS_FMT_TABLE_HIDE_DATAFRAME_SHAPE_INFORMATION"] = "1"


class DataFunction:

    def __init__(
        self,
        df: pl.DataFrame,
        dims: dict[str, DataType],
        dtype: DataType,
        expr: pl.Expr
    ):
        self.df = df
        self.dims = dims
        self.dtype = dtype
        self.expr = expr
        self.name = self.expr.meta.output_name()

    def _computed_df(self) -> pl.DataFrame:
        return self.df.select(list(self.dims.keys()) + [self.expr])

    def _anchor_id(self) -> str:
        return f"{id(self.df)}_{id(self.dims)}"

    def _repr_html_(self) -> str:
        if isinstance(self.dtype, TupleType):
            repr_expr = self.expr.struct.unnest()
        else:
            repr_expr = self.expr

        return f"""<b>{self.name}</b><br>
        <table>
            <tr>
                <th>Dimensions</th>
                <th>Variables</th>
            </tr>
            <tr>
                <td>{self.df.select(self.dims.keys())._repr_html_()}</td>
                <td>{self.df.select(repr_expr)._repr_html_()}</td>
            </tr>
        </table>
        """
    
    def alias(self, name: str) -> 'DataFunction':
        expr = self.expr.alias(name)
        return DataFunction(
            self.df,
            self.dims,
            self.dtype,
            expr
        )

    def join(self, other: 'DataFunction') -> 'DataFunction':
        """Join two functions
        - If a join key is a dimension in both functions (dimension-dimension join), then this key is
            coalesced into a single dimension in the resulting function.
        - If a join key is a dimension in one function and a variable in the other (dimension-variable join), then this
            key is removed as a dimension in the resulting function, since it is uniquely determined by the other dimensions.
        - If a join key is a variable in both functions (variable-variable join), then this is coalesced into a single
            variable in the resulting function.
        """
        if self.name == other.name:
            raise ValueError("Cannot join functions with the same name.")
        
        common_dim_keys = utils.intersection(self.dims.keys(), other.dims.keys())

        if len(common_dim_keys) == 0:
            df = self.df.join(other.df, how="cross")
        else:
            df = self.df.join(
                other.df,
                on=common_dim_keys,
                how="outer",
                coalesce=True,
            )
 
        dim_keys = utils.union(self.dims.keys(), other.dims.keys())
        dims = dict()
        for key in dim_keys:
            if self.dims[key] != other.dims[key]:
                raise ValueError(f"Cannot join functions with same dimension names but different data types: {key} ({self.dims[key]} vs {other.dims[key]})")
            dims[key] = self.dims[key]

        dtype = TupleType([
            Field(self.name, self.dtype),
            Field(other.name, other.dtype)
        ])
        expr = pl.struct([
            self.expr,
            other.expr,
        ]).alias("tuple")

        return utils.make_function(df, dims, dtype, expr)
