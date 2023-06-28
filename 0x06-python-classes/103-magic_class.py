#!/usr/bin/python3

class MagicClass:
    """Initialize a MagicClass for cirile rasius"""

    def __init__(self, radius):
        """initialize variblaes
        Args:
            radius: the radius

        """
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

        def area(self):
            """Return the area of the MagicClass."""
            return (self.__radius ** 2 * math.pi)

        def circumference(self):
            """Return The circumference of the MagicClass."""
            return (2 * math.pi * self.__radius)
