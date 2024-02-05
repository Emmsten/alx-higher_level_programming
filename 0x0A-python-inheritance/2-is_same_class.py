#!/usr/bin/python3
"""Function to check if an object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class; otherwise False"""
    return type(obj) == a_class
