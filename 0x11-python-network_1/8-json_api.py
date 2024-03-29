#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to n-webpage
with the letter as a parameter."""

import requests
import sys

if __name__ == '__main__':

    lett = "" if len(sys.argv) == 1 else sys.argv[1]
    payl = {"q": lett}
    req = requests.post("http://0.0.0.0:5000/search_user", data=payl)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
