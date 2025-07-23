from .base import BaseExpr
from .. import data_types as dt


class TimestampExpr(BaseExpr, dtype=dt.TimestampType):
    pass