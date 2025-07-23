import .data_types as dt

def pl_scalar_to_python(pl_scalar, dtype):
    """
    Convert a Polars scalar to a Python object based on the dtype.
    """
    if pl_scalar is None:
        return None

    if isinstance(dtype, dt.IntegerType):
        return int(pl_scalar)
    elif isinstance(dtype, dt.RealType):
        return float(pl_scalar)
    elif isinstance(dtype, dt.StringType):
        return str(pl_scalar)
    elif isinstance(dtype, dt.BooleanType):
        return bool(pl_scalar)
    else:
        raise TypeError(f"Unsupported dtype: {dtype}")