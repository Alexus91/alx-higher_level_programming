#!/usr/bin/python3
"""function adds attributes to objects."""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible"""
    try:
        setattr(obj, attr, value)
    except AttributeError:
        raise TypeError("can't add new attribute")
