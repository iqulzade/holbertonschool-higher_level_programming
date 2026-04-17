#!/usr/bin/python3
"""
Fetches the status from https://intranet.hbtn.io/status using urllib.
Displays the response body type, content, and decoded UTF-8 string.
"""

import urllib.request
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    req = urllib.request.Request(
        url,
        headers={'cfclearance': 'true'}
    )

    with urllib.request.urlopen(req) as response:
        body = response.read()  # bytes

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
