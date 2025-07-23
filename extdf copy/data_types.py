class DataType:

    def __eq__(self, other):
        if isinstance(other, DataType):
            return str(self) == str(other)
        return False
    
    def __hash__(self):
        return hash(str(self))

class Field:

    def __init__(self, name: str, dtype: DataType):
        self.name = name
        self.dtype = dtype

class IntegerType(DataType):
    def __str__(self):
        return "int"

class RealType(DataType):
    def __str__(self):
        return "real"

class StringType(DataType):
    def __str__(self):
        return "string"

class BooleanType(DataType):
    def __str__(self):
        return "boolean"

class TimestampType(DataType):
    def __str__(self):
        return "timestamp"

class TimedeltaType(DataType):
    def __str__(self):
        return "timedelta"

class IntervalType(DataType):
    def __init__(self, domain: DataType):
        self.domain = domain

    def __str__(self):
        return f"interval[{self.domain}]"

class BallType(DataType):
    def __init__(self, domain: float):
        self.domain = domain

    def __str__(self):
        return "ball"

class TupleType(DataType):
    def __init__(self, fields: dict[str, DataType]):
        self.fields = fields

    def __str__(self):
        string = "("
        string += ", ".join(name for name in self.fields.keys())
        string += ") ["
        string += ", ".join(str(dtype) for dtype in self.fields.values())
        string += "]"
        return string