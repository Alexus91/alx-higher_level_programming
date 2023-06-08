#!/usr/bin/python3
""" prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase
(z in lowercase and Y in uppercase)"""
ind = 0
for char in range(ord('z'), ord('A') - 1, -1):
    x = chr(char - ind)
    print("{}".format(x), end="")
    ind = 32 if ind == 0 else 0
