#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    ct = len(sys.argv) - 1
    if ct == 0:
        print("0 arguments.")
    elif ct == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ct))
    for idx in range(ct):
        print("{}: {}".format(idx + 1, sys.argv[idx + 1]))
