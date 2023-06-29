#!/usr/bin/python3
"""Module that add two integers"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a: type int or float
        b: type int or float

    Return sum of both numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a) if not isinstance(a, int) else a
    b = int(b) if not isinstance(b, int) else b
    return a + b
