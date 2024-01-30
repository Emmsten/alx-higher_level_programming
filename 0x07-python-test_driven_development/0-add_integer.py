#!/usr/bin/python3
"""
Defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a: first integer (default is 0)
    - b: second integer (default is 98)

    Raises:
    - TypeError: If a or b is not an integer or float.

    Returns:
    - Integer: Sum of a and b.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
