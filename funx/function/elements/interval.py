from .base import DataFunction
from abc import ABC, abstractmethod

class AbstractInterval(ABC):

    @classmethod
    @abstractmethod
    def from_endpoints(cls, left, right):
        ...

    @property
    @abstractmethod
    def left(self):
        ...

    @property
    @abstractmethod
    def right(self):
        ...

    def __add__(self, other):
        if isinstance(other, AbstractInterval):
            left = self.left + other.left
            right = self.right + other.right
        else:
            left = self.left + other
            right = self.right + other

        return self.from_endpoints(left, right)



class IntervalFunction(DataFunction, AbstractInterval):

    @classmethod
    def from_endpoints(cls, left: DataFunction, right: DataFunction) -> 'IntervalFunction':
        ...

    @property
    def left(self) -> DataFunction:
        ...

    @property
    def right(self) -> DataFunction:
        ...

    def union(self):
        return self.from_endpoints(self.left.min(), self.right.max())

    def intersection(self):
        return self.from_endpoints(self.left.max(), self.right.min())