import polars as pl
from .data_types import DataType, RealType, IntervalType, TimestampType, TimedeltaType, BallType
import datetime as dt
from functools import wraps


class dispatch:

    REGISTER = list()

    def __init__(self, input_types, output_type):
        self.input_types = input_types
        self.output_type = output_type

    @staticmethod
    def get_type(obj):
        if hasattr(obj, "dtype"):
            return obj.dtype
        return type(obj)

    @staticmethod
    def get_pl_expr(obj):
        if hasattr(obj, "pl_expr"):
            return obj.pl_expr
        return obj

    def __call__(self, func):
        name = func.__name__

        if name not in self.REGISTER:
            self.REGISTER.append((self.input_types, self.output_type, func))

        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(kwargs) > 0:
                raise ValueError("Keyword arguments are not supported in dispatch.")

            if len(args) != len(self.input_types):
                raise ValueError(f"Expected {len(self.inputs)} positional arguments, but got {len(args)}.")

            for input_types, output_type, func in self.REGISTER:
                arg_types = [self.get_type(arg) for arg in args]
                if all(arg_type == input_type for arg_type, input_type in zip(arg_types, input_types)):
                    input_pl_exprs = [self.get_pl_expr(arg) for arg in args]
                    output_pl_expr = func(*input_pl_exprs)
                    return ResolvedExpr(output_pl_expr, name, output_type)
            else:
                raise TypeError(f"No matching function found for types: {[str(self.get_type(arg)) for arg in args]}")

        return wrapper

class String:
    ...

class Int:
    ...

class Real:
    ...

class Timestamp:
    ...

class Timedelta:
    ...

class Interval:
    ...

class Ball:
    ...

class ResolvedExpr:

    def __init__(self, pl_expr: pl.Expr, name: str, dtype: DataType):
        self.pl_expr = pl_expr
        self.name = name
        self.dtype = dtype

    def alias(self, name: str) -> 'ResolvedExpr':
        expr = self.pl_expr.alias(name)
        return ResolvedExpr(expr, name, self.dtype)

    @dispatch((Int, int), Int)
    @dispatch((Int, float), Real)
    @dispatch((Real, int), Real)
    @dispatch((Real, float), Real)
    @dispatch((Timestamp, dt.timedelta), Timestamp)
    @dispatch((Timedelta, dt.timedelta), Timedelta)
    @dispatch((String, str), String)
    def __add__(left, right):
        return left + pl.lit(right)

    @dispatch((Int, Int), Int)
    @dispatch((Int, Real), Real)
    @dispatch((Real, Int), Real)
    @dispatch((Real, Real), Real)
    @dispatch((Timestamp, Timedelta), Timestamp)
    @dispatch((Timedelta, Timedelta), Timedelta)
    @dispatch((String, String), String)
    def __add__(left, right):
        return left + right

    @dispatch((Interval[Timestamp], Timedelta), Interval[Timestamp])
    @dispatch((Interval[Real], Real), Interval[Real])
    def __add__(left, right):
        return pl.struct(
            left=left.struct.field("left") + right,
            right=left.struct.field("right") + right
        )

    @dispatch((Interval[Int], int), Interval[Int])
    @dispatch((Interval[Int], float), Interval[Real])
    @dispatch((Interval[Real], int), Interval[Real])
    @dispatch((Interval[Real], float), Interval[Real])
    @dispatch((Interval[Timestamp], dt.timedelta), Interval[Timestamp])
    def __add__(left, right):
        return pl.struct(
            left=left.struct.field("left") + pl.lit(right),
            right=left.struct.field("right") + pl.lit(right)
        )

    @dispatch(Ball[Real], Ball[Real])
    def union(expr):
        has_unique_center = (expr.struct.field("center").n_unique() == 1)
        valid_expr = pl.struct(
            center=expr.struct.field("center").first(),
            radius=expr.struct.field("radius").max(),
        )
        return pl.when(has_unique_center).then(valid_expr).otherwise(None)