#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """function that finds all multiples of 2 in a list."""
    mul = []
    for number in my_list:
        if number % 2 == 0:
            mul.append(True)
        else:
            mul.append(False)
    return (mul)
