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
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialization method"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Property getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return str(self.print_symbol) * self.width + '\n' * (self.height - 1) + str(self.print_symbol) * self.width

    def __repr__(self):
        """Returns a string representation of the rectangle
        that can be used to create a new instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Destructor method"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

if __name__ == "__main__":
    # Example usage
    r1 = Rectangle(3, 4)
    print(r1)
    print(repr(r1))
    del r1
    print(Rectangle.number_of_instances)
