#!/usr/bin/python3
"""Python script that fetches from a url"""

if __name__ == "__main__":
	import urllib.request

	url = 'https://alx-intranet.hbtn.io/status'
	with urllib.request.urlopen(url) as response:
		content_type = response.headers.get('Content-Type')
		if 'charset=' in content_type:
			encoding = content_type.split('charset=')[1]
		html = response.read()
		utf_type = html.decode(encoding)

	print("Body response:")
	print("\t- type: {}".format(type(html)))
	print("\t- content: {}".format(html))
	print("\t- utf8 content: {}".format(utf_type))
