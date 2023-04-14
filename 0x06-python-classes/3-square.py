#!/usr/bin/python3
"""Defining a class (Square)"""


class Square:
    """Representing a class Square
    Attribute:
        __size (int): A private instance attribute
    """
    def __init__(self, size=0):
        """Initializing a square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    """Representing a public instance attribute """
    def area(self):

        return self.__size ** 2
