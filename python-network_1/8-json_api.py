#!/usr/bin/python3
"""
Sends a POST request and handles JSON response.
"""

import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    r = requests.post("http://0.0.0.0:5000/search_user",
                      data={'q': letter})

    try:
        data = r.json()

        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
