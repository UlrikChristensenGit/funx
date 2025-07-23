from .base import DataFunction
from .real import RealFunction


class IntFunction(DataFunction):

    @register_add
    def _(self, other):
        return [
            (IntFunction, IntFunction, self + other),
        ]
    
    @register_sub
    def _(self, other):
        return [
            (IntFunction, IntFunction, self - other),
        ]
    
    @register_mul
    def _(self, other):
        return [
            (IntFunction, IntFunction, self * other),
        ]
    
    @register_div
    def _(self, other):
        return [
            (IntFunction, RealFunction, self / other),
        ]
    
    @register_pow
    def _(self, other):
        return [
            (RealFunction, RealFunction, self ** other),
            (IntFunction, RealFunction, self ** other),
        ]
    
    @register_sum
    def _(self):
        return [
            (IntFunction, self.sum())
        ]