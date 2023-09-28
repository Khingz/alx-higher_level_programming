#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Peak function"""
    if not isinstance(list_of_integers, list) or len(list_of_integers) < 1:
        return None
    for i in range(len(list_of_integers) - 1):
        if list_of_integers[i] >= list_of_integers[i+1]:
            return list_of_integers[i]
    return list_of_integers[-1]
