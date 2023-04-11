#!/usr/bin/python3
"""Definging a class(Robot)"""

class Robot:
    """Representing a class robot
    Attribute:
        name (str): Robot's identity
        age (int): How old the robot is"""
    def __init__(self, name=None, age=0):
        """Initiallizing class Robot"""
        self.name = name
        self.age = age

"""Creating an Object"""
rob1 =Robot()
rob1.name = "Prince"
rob1.age = 65

print(rob1.age, rob1.name)