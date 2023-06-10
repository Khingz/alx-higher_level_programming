#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if isinstance(my_list, list):
        mul_2 = []
        for n in my_list:
            if n % 2 == 0:
                mul_2.append(True)
            else:
                mul_2.append(False)
        return mul_2
