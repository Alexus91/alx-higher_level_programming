#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print("{}".format(n))
    else:
        print("{0:02}".format(n), end=", ")
