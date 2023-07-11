#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str()"""
        strr = "[" + str(self.__class__.__name__) + "] "
        strr += str(self.__width) + "/" + str(self.__height)
        return strr
