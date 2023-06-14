#!/usr/bin/python3

def weight_average(my_list=[]):
    if isinstance(my_list, list) and len(my_list) != 0:
        deno = 0
        numer = 0
        for num in my_list:
            a, b = num
            deno += b
            numer += (a * b)
        return (numer / deno)
    return (0)
