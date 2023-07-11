#!/usr/bin/python3
"""Module hat returns an object (Python) represented by a JSON"""
import json


def from_json_string(my_str):
    """function that returns an object"""
    return json.loads(my_str)
