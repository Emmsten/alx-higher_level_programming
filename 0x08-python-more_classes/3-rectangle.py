#!/usr/bin/python3

"""
This module contains a class Rectangle

>>> Rectangle = __import__('3-rectangle').Rectangle

>>> my_rectangle = Rectangle(2, 4)
>>> print(type(my_rectangle))
<class '3-rectangle.Rectangle'>

>>> dict_result = my_rectangle.__dict__
>>> print(dict(sorted(dict_result.items())))
{'_Rectangle__height': 4, '_Rectangle__width': 2}

"""


class Rectangle:
    """Class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class.

        Args:
            width (int, optional): The width of the rectangle. Default is 0.
            height (int, optional): The height of the rectangle. Default is 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Public method to calculate the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Public method to calculate the rectangle perimeter."""
        return 2 * (self.__width + self.__height) if self.__width and self.__height else 0

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join("#" * self.__width for _ in range(self.__height))

