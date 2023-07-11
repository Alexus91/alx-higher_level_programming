#!/usr/bin/python3
"""the class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance or inherited instance of the class"""
    if isinstance(obj, a_class):
        return True
    return False
