#!/usr/bin/python3
"""Lazy matrix multiplication"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies marices with numpy library.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """
    return np.matmul(m_a, m_b)
