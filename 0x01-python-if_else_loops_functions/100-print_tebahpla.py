#!/usr/bin/python3

"""prints the ASCII alphabet, in reverse order,
alternating lowercase and uppercase (z in lowercase and Y in uppercase) """
ind = 0
for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char - ind)), end="")
    ind = 32 if ind == 0 else 0
