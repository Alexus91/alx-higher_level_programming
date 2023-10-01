#!/usr/bin/python3
"""takes URL, sends request to URL and display value of the X-Request-Id"""

import sys
import urllib.request

if __name__ == '__main__':

    page = sys.argv[1]
    requ = urllib.request.Request(page)
    with urllib.request.urlopen(requ) as response:
        print(dict(response.headers).get("X-Request-Id"))
