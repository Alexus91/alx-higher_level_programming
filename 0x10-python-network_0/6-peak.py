#!/usr/bin/python3
"""
Find Peak task 6
"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    midd = int(size / 2)
    pea = list_of_integers[midd]
    if pea > list_of_integers[midd - 1] and pea > list_of_integers[midd + 1]:
        return pea
    elif pea < list_of_integers[midd - 1]:
        return find_peak(list_of_integers[:midd])
    else:
        return find_peak(list_of_integers[midd + 1:])
