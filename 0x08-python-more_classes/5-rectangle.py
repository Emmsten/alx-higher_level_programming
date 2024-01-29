class Rectangle:
    """This is a class Rectangle with instance attributes height and width"""

    def __init__(self, width=0, height=0):
        """
        Initializes height and width of the rectangle
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

    @property
    def width(self):
        """Property getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter for the width
        checks if the type for the width is an integer or < 0
        if above conditions aren't met errors are raised
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter for the height
        checks if the type for the height is an integer or < 0
        if above conditions aren't met errors are raised
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        The method area() returns the area of the rectangle
        by taking the product of the width and height of the
        rectangle instance

        >>> my_rectangle = Rectangle(5, 8)
        >>> my_rectangle.area()
        40
        """
        return self.width * self.height

    def perimeter(self):
        """
        The method perimeter() return the perimeter of the
        rectangle by taking the sum of width and height of the
        rectangle, then multiplying the result by 2

        If the width or height of the rectangle is 0 the 0 is
        returned

        >>> my_rectangle = Rectangle(5, 8)
        >>> my_rectangle.perimeter()
        26
        >>> my_rectangle.height = 0
        >>> my_rectangle.perimeter()
        0
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        The method __str__() is used to return the representation (drawing)
        of the rectangle instance using #

        If the width or the height is 0 an empty string is returned
        """
        if self.width == 0 or self.height == 0:
            return ""
        shape_rep_array = []
        for _ in range(self.height):
            shape_rep_array.append("#" * self.width)
            shape_rep_array.append("\n")
        shape_rep_array.pop()
        return "".join(shape_rep_array)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
