#!/usr/bin/python3
"""comment"""

if __name__ == "__main__":
    import requests
    import sys

    user = sys.argv[2]
    repo = sys.argv[1]

    payload = {'committer': 'rails', 'per_page': 10}

    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    res = requests.get(url)
    if res.status_code == 200:
        try:
            res = res.json()
            for i in range(10):
                print("{}: {}".format(
                    res[i]['sha'],
                    res[i]['commit']['author']['name']))
        except ValueError:
            pass