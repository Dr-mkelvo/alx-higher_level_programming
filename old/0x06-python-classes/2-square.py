#!/usr/bin/python3
"""Defining a class (square)"""


class Square:
    """Representing a square
    Attribute:
        __size (int: A private instance attribute)
    """
    def __init__(self, size = 0):
        """Initializing a Square
        Args:
            Size(int): Size of the square
        """
        if not isinstance(self, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
