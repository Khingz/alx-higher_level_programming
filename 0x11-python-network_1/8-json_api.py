#!/usr/bin/python3
"""Comment"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 2:
        data = ""
    else:
        data = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    params = {"q": data}
    res = requests.post(url, data=params)
    if res.status_code == 200:
        try:
            result = res.json()
            if result == {}:
                print("No result")
            else:
                print("[{}] {}".format(result['id'], result['name']))
        except json.JSONDecodeError:
            print('Not a valid JSON')
