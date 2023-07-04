#!/usr/bin/python3
"""Rectangle class."""

class Rectangle:
    """Rectangle representation."""


    def __init__(self, width=0, height=0):
        """new rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter"""
        return (2 * (self.__width + self.__height))
