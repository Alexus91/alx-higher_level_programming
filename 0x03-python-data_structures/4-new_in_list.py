#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific position
    without modifying the original list """
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    cp = [s for s in my_list]
    cp[idx] = element
    return (cp)
