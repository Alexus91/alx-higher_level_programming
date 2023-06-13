#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the biggest integer of a list. """
    if not my_list:
        return None
    mx_val = my_list[0]
    for number in my_list:
        if number > mx_val:
            mx_val = number
    return (mx_val)
