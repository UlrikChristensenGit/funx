from .base import Base


class Vector(Base):

    def __init__(self, *args, fields: dict[str, type[Base]], **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = fields

    @classmethod
    def from_elements(cls, elements: dict[str, Base]) -> 'Vector':
        pl_expr = pl.struct([
            v.pl_expr.alias(k) for k, v in elements.items()
        ])

        fields = {k: v.__class__ for k, v in elements.items()}
        # nested fields???

    def __add__(self, other):
        if isinstance(other, Vector):

            if set(self.names) != set(other.names):
                raise ValueError("Cannot add tuples with different fields.")

            mapping = {name: self[name] + other[name] for name in self.names}
        else:
            mapping = {name: self[name] + other for name in self.names}

        return self.from_elements(mapping)

    def sum(self):
        mapping = {name: elem.sum() for name, elem in self.items()}
        return self.from_elements(mapping)