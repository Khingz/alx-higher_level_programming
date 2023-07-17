#!/usr/bin/python3
"""Py file containing rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Reactangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x attribute"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y attribute"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """computes area of a triangle"""
        return self.__width * self.__height

    def display(self):
        """prints rectangle as block"""
        for _ in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """prints class infp to stdout"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
                )

    def update(self, *args, **kargs):
        """update the values of the class"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for elem in kargs.keys():
                if hasattr(self, elem):
                    setattr(self, elem, kargs[elem])

    def to_dictionary(self):
        """returns dict rep"""
        """return self.__dict__"""
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
        }
