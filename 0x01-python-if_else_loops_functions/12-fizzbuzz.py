#!/usr/bin/python3
def fizzbuzz():
    """ prints the numbers from 1 to 100 separated by a space. """
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end="")
        elif n % 3 == 0:
            print("Fizz", end="")
        elif n % 5 == 0:
            print("Buzz", end="")
        else:
            print(n, end="")
