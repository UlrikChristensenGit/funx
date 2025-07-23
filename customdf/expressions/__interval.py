from .base import Base
import polars as pl
from .composite import Composite

class Interval(Base, metaclass=Composite):

    Domain : type[Base] = ...

    @classmethod
    def from_endpoints(cls, left: Domain, right: Domain) -> 'Interval':
        return cls(pl.struct(
            left.pl_expr.alias("left"),
            right.pl_expr.alias("right")
        ))

    @property
    def left(self) -> Domain:
        return self.Domain(self.pl_expr.struct.field("left"))

    @property
    def right(self) -> Domain:
        return self.Domain(self.pl_expr.struct.field("right"))

    def union(self):
        return self.from_endpoints(self.left.min(), self.right.max())

    def intersection(self):
        return self.from_endpoints(self.left.max(), self.right.min())
    
    def __add__(self, other):
        if isinstance(other, Interval[...]):
            left = self.left + other.left
            right = self.right + other.right
        else:
            left = self.left + other
            right = self.right + other

        return self.from_endpoints(left, right)
