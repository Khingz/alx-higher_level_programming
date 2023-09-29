#!/usr/bin/python3
"""Comment"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
