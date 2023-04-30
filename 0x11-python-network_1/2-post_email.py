#!/usr/bin/python3
"""
    Write a Python script that takes in a URL
    And an email, sends a POST request to the passed URL
    With the email as a parameter,
    And displays the body of the response (decoded in utf-8)
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    body = urllib.parse.urlencode({'email': argv[2]})
    body = body.encode('ascii')
    with urllib.request.urlopen(argv[1], body) as url:
        print(url.read().decode('utf-8'))
