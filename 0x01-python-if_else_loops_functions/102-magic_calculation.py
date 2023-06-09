#!/usr/bin/python3
def magic_calculation(a, b, c):
    """ matching Python bytecode"""
    if a < b:
        return (c)
    elif c > b:
        return (a + b)
    else:
        x = a * b - c
        return (x)
