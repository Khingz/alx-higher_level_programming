#!/usr/bin/python3
def remove_char_at(str, n):
    if n > (len(str) - 1) or n < 0:
        return str
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str
