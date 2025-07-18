from funx.expressions.unresolved import UnresolvedExpression
from funx.mlp.expressions import Expression
import polars as pl








class PCFunction:
    """Represents a n-variate function with following characteristics:
    - It is defined on a collection of non-overlapping n-rectangles.
    - On each n-rectangle, it is a multiplicative seperable function.

    Args:
        pl_df (pl.DataFrame): The polars DataFrame containing the function data.
        dims (dict[str, str]): Mapping of dimension names to their
            set types (e.g. "interval" or "point")
        vars (dict[str, dict[str, str]]): Mapping of variables names to a mapping
            of dimension names to their function types (e.g. "linear" or "constant").
    """

    def __init__(self, pl_df: pl.DataFrame, dims: dict[str, str], vars: dict[str, dict[str, str]]):
        self.pl_df = pl_df
        self.dims = dims
        self.vars = vars

    def select(self, exprs: list[UnresolvedExpression]) -> "PCFunction":
        """Select expressions from the function."""
        pass