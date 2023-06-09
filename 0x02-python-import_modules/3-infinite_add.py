#!/usr/bin/python3

if __name__ == "__main__":
    """Printing additions of all arguments."""
    import sys
    summ = 0
    for inx in range(len(sys.argv) - 1):
        summ += int(sys.argv[inx + 1])
    print("{}".format(summ))
