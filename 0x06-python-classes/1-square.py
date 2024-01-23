#!/usr/bin/python3

class Square:
    """
    Class Square that defines a square.

    Attributes:
        __size (int): Private instance attribute for the size of the square.
    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Note:
            This method does not perform type or value verification on size.
        """
        self.__size = size

