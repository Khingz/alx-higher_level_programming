#!/usr/bin/python3
"""Prints indentations from a given string"""


def text_indentation(text):
    """
    Print text in formatted manner(indentation)

    Args:
        text: text to print

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""

    for ch in text:
        current_line += ch
        if ch == "\n":
            print(current_line.strip())
            current_line = ""
        elif ch in ".:?":
            print(current_line.strip())
            print('')
            current_line = ''
    print(current_line.strip(), end='')
