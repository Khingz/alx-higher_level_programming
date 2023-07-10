#!/usr/bin/python3
"""A function that retrns method and attr of a class"""


def lookup(obj):
    """
    Returns the list obj containing methods and attribute of class
    
    Args:
        obj: object to print method and attributes
    """
    return dir(obj)
