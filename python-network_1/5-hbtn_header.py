#!/usr/bin/python3
"""
Sends a request and displays the X-Request-Id header using requests.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
