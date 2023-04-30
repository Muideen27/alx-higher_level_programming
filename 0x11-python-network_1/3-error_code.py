#!/usr/bin/python3
"""
    Write a Python script that takes in a URL,
    Sends a request to the URL and displays the body;
    Of the response (decoded in utf-8).
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as url:
            print(url.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        error_code = str(e).split(' ')[2][:-1]
        print("Error code: " + str(error_code))
