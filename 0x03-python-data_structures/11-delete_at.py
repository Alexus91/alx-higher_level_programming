#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """ deletes the item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    nw = []
    for i in range(len(my_list)):
        if i != idx:
            nw.append(my_list[i])
    return (nw)
