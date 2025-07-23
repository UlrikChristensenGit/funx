def areinstances(objs: tuple[object], classes_or_list: tuple | list[tuple]) -> bool:
    """Generalization of the `isinstance` method, checking
    a tuple of objects against a tuple of classes or a list
    of the latter.

    Args:
        objs (tuple[object]): Tuple of objects
        classes_or_list (tuple | list[tuple]): Tuple(s) of classes
    """
    if isinstance(classes_or_list, list):
        return any(areinstances(objs, classes) for classes in classes_or_list)
    
    return all(
        isinstance(obj, cls) for obj, cls in zip(objs, classes_or_list)
    )