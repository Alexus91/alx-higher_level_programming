#!/usr/bin/python3
"""script that takes in a string and sends a search request to the SW API"""

from requests import get
from sys import argv

if __name__ == "__main__":

    r = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
