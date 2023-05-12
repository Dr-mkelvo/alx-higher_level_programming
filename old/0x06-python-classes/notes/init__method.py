#!/usr/bin/python3
"""Defining a Person class"""


class Person:
    """Representing a class (Person)
    Attribute:
        Name(Str): The name of the person
    """
    def __init__(self, name):
        """Initializing a person's class"""
        self.name = name

    """Creating a greetings Method"""
    def greetings(self):
        print("Hello {}".format(self.name))

"""Creating an Object"""
p = Person("Prince")
p.greetings()
