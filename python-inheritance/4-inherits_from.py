#!/usr/bin/python3
"""
Returns True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    """

    if isinstance(obj, a_class):
        return False
    for base in type(obj).__bases__:
        if base == a_class:
            return True
        if inherits_from(base, a_class):
            return True
    return False
