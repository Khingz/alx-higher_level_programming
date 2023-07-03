#!/usr/bin/python3
"""Prints a matrix of givrn height and width"""


def print_square(size):
    """
    Prints a square of size <size>

    Args:
        size: size of matrix

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
