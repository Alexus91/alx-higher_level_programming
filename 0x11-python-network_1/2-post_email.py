#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)"""

import sys
import urllib.parse
import urllib.request

if __name__ == '__main__':

    page = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')

    requ = urllib.request.Request(page, data)
    with urllib.request.urlopen(requ) as response:
        print(response.read().decode('utf-8'))