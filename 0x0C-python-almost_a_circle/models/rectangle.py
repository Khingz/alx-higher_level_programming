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

    def update(self, *args, **kwargs):
        """update the values of the class"""
        if args and len(args) != 0:
            arg_count = 0
            for arg in args:
                if arg_count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif arg_count == 1:
                    self.width = arg
                elif arg_count == 2:
                    self.height = arg
                elif arg_count == 3:
                    self.x = arg
                elif arg_count == 4:
                    self.y = arg
                arg_count += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

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
