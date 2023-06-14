#!/usr/bin/python3

def weight_average(my_list=[]):
    deno = 0;
    numer = 0;
    for  num in my_list:
        a, b = num
        deno += b
        numer += (a * b)
    return (numer / deno)
