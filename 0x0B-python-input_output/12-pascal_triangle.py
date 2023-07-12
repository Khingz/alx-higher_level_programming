#!/usr/bin/python3
"""A module that defined a pascal triangle function"""


def pascal_triangle(n):
    """A function that returns a pascal tringle"""
    if n < 1:
        return []
    triangle = [[1]]
    for i in range(1, n):
        zero_triangle = [0] + triangle[i - 1] + [0]
        elem = []
        for j in range(len(zero_triangle) - 1):
            elem.append(zero_triangle[j] + zero_triangle[j + 1])
        triangle.append(elem)
    return triangle
