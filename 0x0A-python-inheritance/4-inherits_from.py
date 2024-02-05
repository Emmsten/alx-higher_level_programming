#!/usr/bin/python3
"""Function to check if an object inherits from a specified class"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class inherited (directly or indirectly) from a_class; otherwise False"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
