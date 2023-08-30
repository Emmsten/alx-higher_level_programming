#!/usr/bin/python3
"""
This module defines the class for calulating the square.
"""


class Square:
    """
    This class embodies the concept of a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        This calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
