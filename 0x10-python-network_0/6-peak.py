#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Peak function"""
    if not isinstance(list_of_integers, list) or \
            len(list_of_integers) < 1:
        return None
    return peak_helper(list_of_integers, len(list_of_integers) - 1, 0)


def peak_helper(item, upper, lower):
    """peak helper function"""
    mid = (lower + upper) // 2
    if (mid == 0 or item[mid] >= item[mid] - 1) and \
            (mid == len(item) - 1 or item[mid] >= item[mid + 1]):
        return item[mid]

    if (mid > 0 and item[mid - 1] > item[mid]):
        return peak_helper(item, mid - 1, lower)
    return peak_helper(item, upper, mid + 1)
