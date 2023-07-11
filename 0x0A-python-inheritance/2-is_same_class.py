#!/usr/bin/python3
""" a class-checking function."""


def is_same_class(obj, a_class):
    """Check the object is exactly an instance of the class."""

    if type(obj) == a_class:
        return True
    return False
