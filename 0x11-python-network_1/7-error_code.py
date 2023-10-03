#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body"""

import sys
import requests

if __name__ == '__main__':

    page = sys.argv[1]
    req = requests.get(page)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
