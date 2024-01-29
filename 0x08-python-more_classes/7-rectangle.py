#!/usr/bin/python3

"""
This module contains a class Rectangle

>>> Rectangle = __import__('7-rectangle').Rectangle

>>> my_rectangle = Rectangle(2, 4)
>>> print(type(my_rectangle))
<class '7-rectangle.Rectangle'>

>>> dict_result = my_rectangle.__dict__
>>> print(dict(sorted(dict_result.items())))
{'_Rectangle__height': 4, '_Rectangle__width': 2}

"""


class Rectangle:
    """This is an class Rectangle with instance attribute height and width"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        initializes height and width of the rectangle
        upon creation of an instance using property
        getters and setters

        >>> my_rectangle = Rectangle(2, '4')
        Traceback (most recent call last):
            ...
        TypeError: height must be an integer


        >>> my_rectangle = Rectangle(0, 0)
        >>> my_rectangle.width = 10
        >>> my_rectangle.height = -3
        Traceback (most recent call last):
            ...
        ValueError: height must be >= 0
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        shape_rep_array = []
        for height in range(self.height):
            shape_rep_array.append(self.print_symbol * self.width)
            shape_rep_array.append("\n")
        shape_rep_array.pop()
        return "".join(shape_rep_array)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Bye re
