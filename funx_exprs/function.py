import polars as pl
from typing import Literal, Any
import os
os.environ["POLARS_FMT_TABLE_HIDE_DATAFRAME_SHAPE_INFORMATION"] = "1"

class Expression:
    pass


def as_exprs(exprs: list[str | pl.Expr]) -> list[pl.Expr]:
    """Convert a list of strings or polars expressions to a list of polars expressions."""
    casted_exprs = []
    for expr in exprs:
        if isinstance(expr, str):
            casted_exprs.append(pl.col(expr))
        elif isinstance(expr, pl.Expr):
            casted_exprs.append(expr)
        else:
            raise TypeError(f"Expected str or pl.Expr, got {type(expr)}")
    return casted_exprs

def intersection(a: list, b: list) -> list:
    """Return the intersection of two lists."""
    return list(set(a).intersection(set(b)))

def union(a: list, b: list) -> list:
    """Return the union of two lists."""
    return list(set(a).union(set(b)))

def duplicates(a: list) -> list:
    """Return a list of duplicates in a list."""
    seen = []
    duplicates = []
    for item in a:
        if item in seen:
            duplicates.append(item)
        else:
            seen.append(item)
    return duplicates


class DataFunction:

    def __init__(
        self,
        df: pl.DataFrame,
        dims: list[str],
        vars: list[str],
    ):
        self.df = df
        self.dims = dims
        self.vars = vars

    @property
    def fields(self) -> list[str]:
        return self.dims + self.vars

    def __repr__(self) -> str:
        return f"Dimensions\n: {self.df.select(self.dims)}\nVariables\n: {self.df.select(self.vars)}"

    def _repr_html_(self) -> str:
        return f"""<table>
            <tr>
                <th>Dimensions</th>
                <th>Variables</th>
            </tr>
            <tr>
                <td>{self.df.select(self.dims)._repr_html_()}</td>
                <td>{self.df.select(self.vars)._repr_html_()}</td>
            </tr>
        </table>
        """

    def select(self, exprs: list[str | pl.Expr]) -> 'DataFunction':
        """Select new variables from existing dimensions and variables."""
        exprs = as_exprs(exprs)

        new_vars = [expr.meta.output_name() for expr in exprs]

        # check if any new variables names conflict with existing dimension namess
        overlapping_vars_and_dims = intersection(new_vars, self.dims)
        if len(overlapping_vars_and_dims) > 0:
            raise ValueError(f"Variable names {overlapping_vars_and_dims} conflict with dimension names.")

        new_df = self.df.select(self.dims + exprs)
        return DataFunction(new_df, self.dims, new_vars)

    def filter(self, predicate: Expression) -> 'DataFunction':
        """Filter out data matching a given predicate."""
        new_df = self.df.filter(predicate)
        return DataFunction(new_df, self.dims, self.vars)

    def rename(self, mapping: dict[str, str]) -> 'DataFunction':
        """Rename fields (both dimensions and variables)"""

        # check if any fields are renamed to the same name
        duplicated_renamings = duplicates(mapping.values())
        if len(duplicated_renamings) > 0:
            raise ValueError(f"Cannot rename fields to the same names: {duplicated_renamings}.")

        new_dims = [mapping.get(dim, dim) for dim in self.dims]
        new_vars = [mapping.get(var, var) for var in self.vars]
        new_df = self.df.rename(mapping)
        return DataFunction(new_df, new_dims, new_vars)

    def head(self, n: int, along: str) -> 'DataFunction':
        new_df = (
            self.df
            .sort(by=along)
            .tail(n)
        )
        return DataFunction(new_df, self.dims, self.vars)

    def tail(self, n: int, along: str) -> 'DataFunction':
        new_df = (
            self.df
            .sort(by=along)
            .head(n)
        )
        return DataFunction(new_df, self.dims, self.vars)

    def sum(self, along: list[str] = None) -> 'DataFunction':
        if along is None:
            along = self.dims
    
        for field in along:
            if field not in self.dims:
                raise ValueError(f"Cannot aggregate along '{field}' as this is not a dimension.")

        remaining_dims = [dim for dim in self.dims if dim not in along]

        if len(remaining_dims) == 0:
            return self.df.select(self.vars).sum().to_dicts()[0]

        new_df = (
            self.df
            .group_by(remaining_dims)
            .agg([pl.sum(var).alias(var) for var in self.vars])
        )

        return DataFunction(new_df, remaining_dims, self.vars)
    


    def join(
        self,
        other: 'DataFunction',
        on: list[str] = None,
        how: Literal["inner", "left", "right", "outer", "leftsemi", "rightsemi", "leftanti", "rightanti", "cross"] = "outer",
    ) -> 'DataFunction':
        """Join two functions
        - If a join key is a dimension in both functions (dimension-dimension join), then this key is
          coalesced into a single dimension in the resulting function.
        - If a join key is a dimension in one function and a variable in the other (dimension-variable join), then this
          key is removed as a dimension in the resulting function, since it is uniquely determined by the other dimensions.
        - If a join key is a variable in both functions (variable-variable join), then this is coalesced into a single
          variable in the resulting function.
        """
        if on is None:
            on = []
    
        shared_fields = set(self.fields).intersection(set(other.fields)).difference(on)

        if len(shared_fields) > 0:
            renamed_self = self.rename({field: f"{field}_left" for field in shared_fields})
            renamed_other = other.rename({field: f"{field}_right" for field in shared_fields})
            return renamed_self.join(renamed_other, on=on, how=how)
 
        if len(on) == 0:
            new_df = self.df.join(
                other.df,
                how="cross",
            )
        else:
            new_df = self.df.join(
                other.df,
                on=on,
                how=how,
                coalesce=True,
            )

        # cases:
        # - join key is a dimension in both DataFunctions
        #   - this is coerced into a single dimension of that name
        # - join key is a dimension in one DataFunction and a variable in the other
        #  - this is removed as a dimension, since it is uniquely determined by the one data function
        # - join key is a variable in both DataFunctions
        #  - this is not allowed
        new_dims = list(set(self.dims + other.dims))
        for field in on:
            if field in new_dims:
                if (field in self.vars and field in other.dims) or (field in other.vars and field in self.dims):
                    new_dims.remove(field)

        new_vars = list(set(self.vars + other.vars))
                
        return DataFunction(new_df, new_dims, new_vars)



    def slice(self, dim: str, at: Any) -> 'DataFunction':
        pass


