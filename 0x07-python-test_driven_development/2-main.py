#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 3]
]
a = [[3, 9], [12, 15, 3]]
matrix1 = [[]]
print(matrix_divided(a, 3))
print(matrix_divided(matrix, 2))
print(matrix)
