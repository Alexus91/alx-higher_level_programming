#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == '__main__':
    url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(url) as response:
        bd = response.read()

        print("Body response:")
        print("    - type: {}".format(type(bd)))
        print("    - content: {}".format(bd))
        print("    - utf8 content: {}".format(bd.decode('utf8')))
