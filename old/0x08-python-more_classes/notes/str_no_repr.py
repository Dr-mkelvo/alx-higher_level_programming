#!/usr/bin/python3
"""Defining a class A"""


class A:
    def __str__(self):
        return "42"

"""Creating an Object"""
a = A()
print(repr(a))
print(str(a))