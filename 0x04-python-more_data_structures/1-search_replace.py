#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces an element by another in a new list"""
    nwlist= list(map(lambda x: replace if x == search else x, my_list))
    return (nwlist)
