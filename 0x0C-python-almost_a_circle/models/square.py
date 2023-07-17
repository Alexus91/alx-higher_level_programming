#!/usr/bin/python3
""" New class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns printed string of an instance """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    def update(self, *args, **kwargs):
        """Update the class Square by adding the public method"""
        if args and len(args) > 0:
            attr_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
