#!/usr/bin/python3
"""Comment"""

if __name__ == "__main__":
	import requests

	url = 'https://alx-intranet.hbtn.io/status'
	res = requests.get(url)
	print("Body response:")
	print("\t- type: {}".format(type(res.text)))
	print("\t- content: {}".format(res.text))