#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string."""
    cp = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(cp))
