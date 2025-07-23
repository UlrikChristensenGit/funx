from .base import BaseExpr
import polars as pl
from ..data_types import IntervalType


class IntervalExpr(BaseExpr, dtype=IntervalType):

    @classmethod
    def from_endpoints(cls, left: BaseExpr, right: BaseExpr) -> 'IntervalExpr':
        if left.dtype != right.dtype:
            raise TypeError(f"Endpoints must have the same data type ({left.dtype} != {right.dtype}")

        pl_expr = pl.struct(
            left.pl_expr.alias("left"),
            right.pl_expr.alias("right")
        )
        dtype = IntervalType(left.dtype)

        return cls.from_polars(pl_expr, dtype)

    @property
    def left(self) -> BaseExpr:
        pl_expr = self.pl_expr.struct.field("left")
        dtype = self.dtype.domain
        return self.from_polars(pl_expr, dtype)

    @property
    def right(self) -> BaseExpr:
        pl_expr = self.pl_expr.struct.field("right")
        dtype = self.dtype.domain
        return self.from_polars(pl_expr, dtype)

    def union(self):
        return self.from_endpoints(self.left.min(), self.right.max())

    def intersection(self):
        return self.from_endpoints(self.left.max(), self.right.min())

    def __add__(self, other):
        if isinstance(other, IntervalExpr):
            left = self.left + other.left
            right = self.right + other.right
        else:
            left = self.left + other
            right = self.right + other

        return self.from_endpoints(left, right)

    def isoformat(self) -> BaseExpr:
        self.left.isoformat() + "/" + self.right.isoformat()
