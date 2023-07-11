#!/usr/bin/python3
"""A module that reads a text file"""


def read_file(filename=""):
    """
    Reads a file to stdout

    Args:
        filename: name of file
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line)
