#!/usr/bin/python3
"""prints all possible different combinations of two digits
The two digits must be different"""
for d1 in range(0, 10):
    for d2 in range(d1 + 1, 10):
        if d1 == 8 and d2 == 9:
            print("{}{}".format(d1, d2))
        else:
            print("{}{}".format(d1, d2), end=", ")
