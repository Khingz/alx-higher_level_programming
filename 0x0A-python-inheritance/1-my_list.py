#!/usr/bin/python3
"""A class that inherot from list obj"""


class MyList(list):
    """A class that inherits from list"""
    def __init__(self, *args):
        """
        initializes class, inherit from base class

        Args:
            args: optional argument inherited from base class
        """
        super().__init__(*args)

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
