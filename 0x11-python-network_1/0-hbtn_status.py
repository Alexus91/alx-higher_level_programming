#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:

    bd = response.read()

    print("Body response:")
    print("    - type: {}".format(type(bd)))
    print("    - content: {}".format(bd))
    print("    - utf8 content: {}".format('utf8'))
