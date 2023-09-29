#!/usr/bin/python3
"""comment"""

if __name__ == "__main__":
    import requests
    import sys

    user = sys.argv[2]
    repo = sys.argv[1]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            user,
            repo)
    res = requests.get(url)
    if res.status_code == 200:
        try:
            res = res.json()
            for i in range(min(10, len(res))):
                print("{}: {}".format(
                    res[i].get('sha'),
                    res[i].get('commit').get('author').get('name')))
        except ValueError:
            pass
