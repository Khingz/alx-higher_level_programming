#!/usr/bin/python3
"""Comment"""

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    username = sys.argv[1]
    passwd = sys.argv[2]

    auth = HTTPBasicAuth(username, passwd)
    url = 'https://api.github.com/user'
    res = requests.get(url, auth=auth)
    user_data = res.json()
    print(user_data.get('id'))
