#!/usr/bin/python3
"""Defining a class"""


class A:
    """Representing class"""
    def __repr__(self):
        return "42"

"""Creating an Object"""
a = A()
print(repr(a))
print(str(a))
