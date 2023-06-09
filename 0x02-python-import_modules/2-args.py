#!/usr/bin/python3
if __name__ == "__main__":
    """basic arithmetic operation"""
    from calculator_1 import add, sub, mul, div
    import sys
    number_args = len(sys.argv) - 1
    print("{} argument{}:".format(number_args, 's' if number_args != 1 else ''))
    if number_args > 0:
        for i in range(1, number_args + 1):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("No arguments were passed.")
