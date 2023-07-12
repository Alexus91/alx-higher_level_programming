#!/usr/bin/python3
"""string to JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON as a string object."""
    return json.dumps(my_obj)
