#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    sum = []
    for i in range(2):
        try:
            n_1 = tuple_a[i]
        except IndexError:
            n_1 = 0
        try:
            n_2 = tuple_b[i]
        except IndexError:
            n_2 = 0
        sum.append(n_1 + n_2)
    return tuple(sum)
