#!/usr/bin/python3
"""Perform a matrix multiolication operation"""


def matrix_mul(m_a, m_b):
    """
    A function that prints new matrix from mul of 2 matrix
    Args:
        m_a: first matrix
        m_b: second matrix

    Return: A new list with result of multiplication of m_a and m_b
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(el, list) for el in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(el, list) for el in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise TypeError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise TypeError("m_b can't be empty")

    for li in m_a:
        if not all(isinstance(el, (int, float)) for el in li):
            raise ValueError("m_a should contain only integers or floats")

    for li in m_b:
        if not all(isinstance(el, (int, float)) for el in li):
            raise ValueError("m_b should contain only integers or floats")

    for el in m_a:
        length = len(m_a)
        if len(el) != length:
            raise TypeError("each row of m_a must be of the same size")

    for el in m_b:
        length = len(m_b)
        if len(el) != length:
            raise TypeError("each row of m_b must be of the same size")

    mul_list = []
    row_ma = len(m[0])
    column_mb = 0
    for i in m_b:
        column_mb += 1
    if row_ma != column_mb:
        raise ValueError("m_a and m_b can't be multiplied")

    trans_matrix = list(zip(*ma_b))
    dot_matrix = []
    for r in m_a:
        row = []
        for c in trans_matrix:
            product = 0
            for i in range(len(r)):
                product += r[i] * c[i]
            row.append(product)
        dot_matrix.append(row)

    return dot_matrix
