#!/usr/bin/python3
"""comment"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    encoded_data = urllib.parse.urlencode(data).encode('utf8')
    request = urllib.request.Request(url, data=encoded_data, method='POST')
    with urllib.request.urlopen(request) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)
