#!/usr/bin/python3
"""Comment"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    from urllib.error import HTTPError

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html)
        except HTTPError as e:
            print('Error code: ', e.code)
