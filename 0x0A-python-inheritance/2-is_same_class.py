#!/usr/bin/python3
"""Test if is instance of a class"""


def is_same_class(obj, a_class):
    """Checks an object if is class instance

    Args:
        obj: object
        a_class: class
    Return: True or false
    """
    return True if type(obj) == a_class else False
