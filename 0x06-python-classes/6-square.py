#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square.
    Args:
        size (int): The size of the new square.

    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize propertirs"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """updates the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current area of square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints a square of size attribute"""
        if (self.__size == 0):
            print("")
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
