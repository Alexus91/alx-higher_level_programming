#!/usr/bin/python3
"""the max integer in a list"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers"""

    if len(list) == 0:
        return None
    result = list[0]
    inx = 1
    while inx < len(list):
        if list[inx] > result:
            result = list[inx]
        inx += 1
    return (r)
