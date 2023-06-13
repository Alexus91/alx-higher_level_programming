#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string."""
    for x in my_string:
        if x != 'c' and x != 'C':
            nw_str += x
    return (nw_str)
