#!/usr/bin/python3
"""script that takes a URL, sends a request to the URL and displays the value"""

import sys
import requests

if __name__ == '__main__':

    page = sys.argv[1]
    req = requests.get(page)
    print(req.headers.get("X-Request-Id"))
