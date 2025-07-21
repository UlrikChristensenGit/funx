from funx.function.elements.data_types import DataType, TupleType
import polars as pl

class Schema:

    def __init__(
        self,
        dims: dict[str, DataType],
        name: str,
        dtype: DataType,
    ):
        self.dims = dims
        self.name = name
        self.dtype = dtype

    def __repr__(self):
        string = "Name:\n"
        string += f"\t{self.name}\n"
        string += "Data Type:\n"
        string += f"\t{self.dtype}\n"
        string += "Dimensions:\n"
        string += "\t("
        string += ", ".join(name for name in self.dims.keys())
        string += ") ["
        string += ", ".join(str(dtype) for dtype in self.dims.values())
        string += "]"
        return string
