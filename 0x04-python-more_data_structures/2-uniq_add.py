#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = None
    for i in list(set(my_list)):
        total = (i if total == None else total + i)
    return total
