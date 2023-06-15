#!/usr/bin/python3
def uniq_add(my_list=[]):
    un_list = set(my_list)
    n = 0

    for i in un_list:
        n += i

    return (n)
