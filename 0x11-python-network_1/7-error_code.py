#!/usr/bin/python3
"""
    Python script that takes in a URL,
    Sends a request to the URL and displays;
    he body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
