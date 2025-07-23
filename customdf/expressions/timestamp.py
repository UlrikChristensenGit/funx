from .base import Base
from .timedelta import Timedelta

class Timestamp(Base):

    @register_add
    def _(self, other):
        return [
            (Timedelta, Timestamp, self + other),
        ]

    @register_sub
    def _(self, other):
        return [
            (Timedelta, Timestamp, self - other),
            (Timestamp, Timedelta, self - other),
        ]
