#!/usr/bin/python3
"""module that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a content <text> to file <filename>"""
    with open(filename, 'w') as f:
        return f.write(text)
