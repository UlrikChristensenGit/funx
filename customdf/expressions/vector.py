


class Vector:

    base = ...

    def __add__(self, other):
        if not isinstance(other.base, self.base):
            raise TypeError(f"Cannot add {self.base} to {other.base}")
        




