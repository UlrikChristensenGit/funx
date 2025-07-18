from typing import Protocol, Any


class Tuple(Protocol):
    """
    Protocol for named (mathematical) tuple.
    Based on the built-in `dict` type, but with
    additional mathematical operations used in
    relational algebra.
    """

    def __getitem__(self, key: str) -> Any:
        ...

    def __setitem__(self, key: str, value: Any) -> None:
        ...

    def __len__(self) -> int:
        ...

    def project(self, keys: list[str]) -> "Tuple":
        ...

    def __add__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise addition
        ...

    def __sub__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise subtraction
        ...

    def __mul__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise multiplication
        ...

    def __truediv__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise division
        ...

    def __floordiv__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise floor division
        ...

    def __mod__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise modulo operation
        ...

    def __pow__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise power operation
        ...

    def __eq__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise equality check
        ...

    def __ne__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise inequality check
        ...

    def __lt__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise less than check
        ...

    def __le__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise less than or equal to check
        ...

    def __gt__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise greater than check
        ...

    def __ge__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise greater than or equal to check
        ...

    def __and__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise logical AND operation
        ...

    def __or__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise logical OR operation
        ...

    def __xor__(self, other: "Tuple" | Any) -> "Tuple":
        # element-wise logical XOR operation
        ...

    def __invert__(self) -> "Tuple":
        # element-wise logical NOT operation
        ...
