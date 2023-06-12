#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replaces an element of a list at a specific position"""
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    nw_list = my_list[:]
    nw_list[idx] = element
    return (nw_list)
