#!/usr/bin/python3
"""Defining a class Robot"""


class Robot:
    """Representing a class(Robot)"""
    def __init__(self, name):
        """Initializing robot class
        Args:
            name(str): The name of the robot
        """
        print(name, "has been created!")
    def __del__(self):
        print("BOT Destroyed!!")

"""Creating an Object"""
if __name__ == "__main__":
    x = Robot("RB1")
    y = Robot("RB2")
    z = y
    print("Deleting X")
    del x
    print("Deleting Z")
    del z
    del y