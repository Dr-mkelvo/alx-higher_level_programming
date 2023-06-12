#!/usr/bin/python3
"""Defining a Class (MyList)"""


class MyList(list):
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
