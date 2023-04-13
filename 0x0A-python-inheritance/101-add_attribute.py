#!/usr/bin/python3
"""Defining a method (add_attribute)."""


def add_attribute(obj, att, value):
    """
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
