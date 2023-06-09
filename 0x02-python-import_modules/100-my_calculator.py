#!/usr/bin/python3
if __name__ == "__main__":
    """Build your own calculator"""

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    operations = {"+": add, "-": sub, "*": mul, "/": div}

    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    summ = operations[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, summ))
