#!/usr/bin/python3
"""Test if is instance of a class or object"""


def is_kind_of_class(obj, a_class):
    """Checks an object if is class instance or subclass

    Args:
    obj: object
    a_class: class
    Return: True or false
    """
    return isinstance(obj, a_class)
