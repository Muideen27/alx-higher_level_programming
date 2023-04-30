#!/usr/bin/python3
"""
    Python script that takes in a letter and;
    Sends a POST request to http://0.0.0.0:5000/search_user;
    with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if respone == {}:
            print("No response")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except valueError:
        print("Not a valid JSON")
