#!/usr/bin/python3
"""Defining a method (pascal_triangle)"""


def pascal_triangle(n):
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        tri = tri[-1]
        tmp = [1]
        for x in range(len(tri) - 1):
            tmp.append(tri[x] + tri[x + 1])
        tmp.append(1)
        tri.append(tmp)
    return tri
