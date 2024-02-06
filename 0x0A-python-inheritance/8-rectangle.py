#!/usr/bin/python3
"""
Contains the class BaseGeometry and Rectangle
"""


class BaseGeometry:
    """A class with public attributes area and integer_validator"""
    def area(self):
        """Raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value parameter"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class representing a rectangle"""
    def __init__(self, width, height):
        """Initializes a rectangle with a given width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
