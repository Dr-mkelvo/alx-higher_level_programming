#!/usr/bin/python3
"""Defining a parent class"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
