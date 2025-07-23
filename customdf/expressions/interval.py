from .base import Base
import polars as pl
from ..data_types import IntervalType


class Interval(Base, dtype=IntervalType):

    @classmethod
    def from_endpoints(cls, left: Base, right: Base) -> 'Interval':
        if left.dtype != right.dtype:
            raise TypeError(f"Endpoints must have the same data type ({left.dtype} != {right.dtype}")

        dtype = left.dtype
        pl_expr = pl.struct(
            left.pl_expr.alias("left"),
            right.pl_expr.alias("right")
        )

        return cls.from_polars(pl_expr, dtype)

    @property
    def left(self) -> Base:
        dtype = self.dtype.domain
        pl_expr = self.pl_expr.struct.field("left")
        return self.from_polars(pl_expr, dtype)

    @property
    def right(self) -> Base:
        dtype = self.dtype.domain
        pl_expr = self.pl_expr.struct.field("right")
        return self.from_polars(pl_expr, dtype)

    def union(self):
        return self.from_endpoints(self.left.min(), self.right.max())

    def intersection(self):
        return self.from_endpoints(self.left.max(), self.right.min())

    def __add__(self, other):
        if isinstance(other, Interval):
            left = self.left + other.left
            right = self.right + other.right
        else:
            left = self.left + other
            right = self.right + other

        return self.from_endpoints(left, right)
