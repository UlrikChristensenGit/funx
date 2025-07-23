from .utils import areinstances
from . import data_types as dt
from .expression import Expression

def add(self: Expression, other: Expression):
    operation_table = [
        (dt.IntegerType, dt.IntegerType, dt.IntegerType()),
    ]
    for sdtype_class, odtype_class, rdtype in operation_table:
        if isinstance(self.dtype, sdtype_class) and isinstance(other.dtype, odtype_class):
            return Expression(self.pl_expr + other.pl_expr, rdtype)


    if areinstances(
        (self.dtype, other.dtype),
         [
            (dt.IntegerType(), dt.IntegerType()),
            (dt.RealType(), dt.RealType()),
            (dt.IntegerType(), dt.RealType()),
            (dt.RealType(), dt.IntegerType())
        ]
    ):
        pass

    match (self.dtype, other.dtype):
        case (dt.IntegerType(), dt.IntegerType()):
            return Expression(self.pl_expr + other.pl_expr, dt.IntegerType())
        case (dt.RealType(), dt.RealType()):
            return Expression(self.pl_expr + other.pl_expr, dt.RealType())
        case (dt.IntegerType(), dt.RealType()):
            return Expression(self.pl_expr + other.pl_expr, dt.RealType())
        case (dt.RealType(), dt.IntegerType()):
            return Expression(self.pl_expr + other.pl_expr, dt.RealType())
        case _:
            return NotImplemented
        

def alias(expr: Expression, name: str) -> Expression:
    return Expression(
        pl_expr=expr.pl_expr.alias(name),
        dtype=expr.dtype
    )

