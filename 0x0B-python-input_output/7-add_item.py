#!/usr/bin/python3
"""Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        my_lis = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_lis = []
    my_lis.extend(sys.argv[1:])
    save_to_json_file(my_lis, "add_item.json")
