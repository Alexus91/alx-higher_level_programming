#!/usr/bin/python3
"""locked class """


class LockedClass:
    """
    LockedClass is a class that restricts the dynamic
    creation of instance attributes,
    except for a specific attribute called 'first_name'.
    """

    __slots__ = ['first_name']
