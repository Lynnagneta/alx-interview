#!/usr/bin/python3
""" this is a pascal triangle generating file"""


def pascal_triangle(n):
    """
    prints lists of integers representing the Pascal’s triangle of n
    """
    res = []
    if n > 0:
        """executed only when n is greater than 0"""
        for i in range(1, n + 1):
            new_list = []
            C = 1
            for j in range(1, i + 1):
                new_list.append(C)
                C = C * (i - j) // j
            res.append(new_list)
    return res
