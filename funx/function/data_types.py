class DataType:
    ...

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
    def __init__(self, fields: list[Field]):
        self.fields = fields

    def get(self, name: str) -> Field:
        for field in self.fields:
            if field.name == name:
                return field
        raise KeyError(name)

    def __str__(self):
        string = "("
        string += ", ".join(field.name for field in self.fields)
        string += ") ["
        string += ", ".join(str(field.dtype) for field in self.fields)
        string += "]"
        return string