#!/usr/bin/python3
"""A module that tries ti add attribute to alist"""


def add_attribute(obj, attr_name, value):
    """class that check and set attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
