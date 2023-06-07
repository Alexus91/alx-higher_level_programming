#!/usr/bin/python3
def print_last_digit(number):
    """prints the last digit of a number."""
    r = abs(number) % 10
    print(r, end="")
    return(r)
