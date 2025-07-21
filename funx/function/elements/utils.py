from .data_types import RealType, TupleType, DataType
import polars as pl

def make_function(
    df: pl.DataFrame,
    dims: dict[str, DataType],
    dtype: DataType,
    expr: pl.Expr
):
    from .real import RealFunction
    from .tuple import TupleFunction
    if isinstance(dtype, RealType):
        return RealFunction(df, dims, dtype, expr)
    elif isinstance(dtype, TupleType):
        return TupleFunction(df, dims, dtype, expr)
    else:
        raise TypeError(f"Unsupported data type: {dtype}")

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

