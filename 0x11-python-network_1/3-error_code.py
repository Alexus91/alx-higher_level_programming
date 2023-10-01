#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body."""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    page = sys.argv[1]

    try:
        with urllib.request.urlopen(page) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
