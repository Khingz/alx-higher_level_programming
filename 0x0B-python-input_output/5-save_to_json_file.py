#!/usr/bin/python3
"""Module that writes an Object to a text file, using a JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes Object to file, using a JSON rep"""
    with open(filename, 'w') as f:
        js = json.dumps(my_obj)
        return f.write(js)
