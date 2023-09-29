#!/usr/bin/python3
"""Comment"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    res = requests.get(url)
    request_id = res.headers.get('X-Request-Id')
    print(request_id)
