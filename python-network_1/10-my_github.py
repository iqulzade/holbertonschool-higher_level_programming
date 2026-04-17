#!/usr/bin/python3
"""
Uses GitHub API to display user id using basic authentication.
"""

import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]

    r = requests.get("https://api.github.com/user",
                     auth=(user, token))

    data = r.json()
    print(data.get("id"))
