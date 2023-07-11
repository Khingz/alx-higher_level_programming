#!/usr/bin/python3
"""module that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an obj"""
    return json.dumps(my_obj)
