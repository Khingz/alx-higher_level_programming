#!/usr/bin/python3
"""Comment"""

if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import HTTPError

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf8')
            print(html)
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
