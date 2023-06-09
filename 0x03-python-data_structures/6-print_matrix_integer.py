#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for i in range(len(n)):
            if i != (len(n) - 1):
                print("{} ".format(n[i]), end="")
            else:
                print(n[i], end="")
        print()
