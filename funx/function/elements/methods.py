from .tuple import TupleFunction
from typing import Any
from .base import DataFunction

def combine(mapping: dict[str, Any] | list[Any]) -> DataFunction:
    """Combine objects into a named tuple

    Args:
        mapping (dict[str, Any] | list[Any]): _description_

    Returns:
        DataFunction: _description_
    """