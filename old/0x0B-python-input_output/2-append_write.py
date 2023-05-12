#!/usr/bin/python3
"""Defining a method (append_write)."""


def append_write(filename="", text=""):
    """
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
