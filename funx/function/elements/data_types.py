class DataType:
    
    def __eq__(self, other):
        if isinstance(other, DataType):
            return str(self) == str(other)
        return False

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

class TupleType(DataType):
    def __init__(self, fields: dict[str, DataType]):
        self.fields = fields

    def get(self, name: str) -> Field:
        return self.fields[name]

    def __str__(self):
        string = "("
        string += ", ".join(name for name in self.fields.keys())
        string += ") ["
        string += ", ".join(str(dtype) for dtype in self.fields.values())
        string += "]"
        return string