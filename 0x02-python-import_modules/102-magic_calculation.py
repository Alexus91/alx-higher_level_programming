#!/usr/bin/python3
def magic_calculation(a, b):
    """make it match bytecode provided"""
    from magic_calculation_102 import add, sub
    if a < b:
        cum = add(a, b)
        for i in range(4, 6):
            cum = add(cum, i)
        return cum
    else:
        return sub(a, b)
