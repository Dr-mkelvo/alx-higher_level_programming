#!/usr/bin/python3
"""Defining a method (from_json_string)."""
import json


def from_json_string(my_str):
    return json.loads(my_str)
