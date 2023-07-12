#!/usr/bin/python3
""" text file reading function."""


def read_file(filename=""):
    """Print UTF8 text file to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
