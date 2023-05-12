#!/usr/bin/python3
"""Defining a Function"""


def add_integer(a, b=98):
    """
    args:
        a(int/float): First number
        b(int/float): Second number
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
