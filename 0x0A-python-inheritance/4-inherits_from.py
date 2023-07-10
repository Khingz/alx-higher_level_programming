#!/usr/bin/python3
"""Test if is instance of a class is a subclass"""


def inherits_from(obj, a_class):
    """Checks an object if is subclass

    Args:
    obj: object
    a_class: class
    Return: True or false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
