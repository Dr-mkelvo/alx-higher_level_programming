#!/usr/bin/python3
"""Defining a class"""


class Robot:
    """Representing a class"""
    def __init__(self, name, built_year):
        """Initialization
        Args:
            name(str): The name of the robot
            built_year(int): Year of Manufacture
        """
        self.name = name
        self.built_year = built_year

    def __repr__(self):
        return "Robot ('" + self.name + "', " + str(self.built_year) + ")"

    def __str__(self):
        return "Name: " + self.name + ", Built Year: " + str(self.built_year)


if __name__ == "__main__":
    x = Robot("Marvin", 1999)
    x_str = str(x)
    print(x_str)
    print("Types of X_str: ", type(x_str))
    new = eval(x_str)
    print(new)
    print("Type of New: ", type(new))   