#!/usr/bin/python3
"""Defining a method (load_from_json_file)."""


def write_file(filename="", text=""):
    """
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
