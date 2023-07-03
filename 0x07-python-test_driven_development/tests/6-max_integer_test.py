#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""Unittest for max_integer([..])
"""


class TestMax(unittest.TestCase):
    def test_max_int(self):
        """Test on int"""

        """ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        """unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        """list with negative int"""
        self.assertEqual(max_integer([6, -3, 4, 2]), 6)
        """empty list"""
        self.assertEqual(max_integer([]), None)
        """max at begining"""
        self.assertEqual(max_integer([56, 1, 3, 4, 2]), 56)
        """max at end"""
        self.assertEqual(max_integer([1, 3, 4, 2, 100]), 100)
        """floats list"""
        self.assertEqual(max_integer([2.5, -4.5, 4.5, 2.1]), 4.5)
        """floats and int list"""
        self.assertEqual(max_integer([3, 3.5, -4, 2.1]), 3.5)
        """single list element"""
        self.assertEqual(max_integer([9]), 9)
        """repeated max element"""
        self.assertEqual(max_integer([1, 10, 6, 10, 9]), 10)

    def test_max_str(self):
        """Test on strings"""

        """empty string"""
        self.assertEqual(max_integer(""), None)
        """#lowercase strings"""
        self.assertEqual(max_integer("hello world"), "w")
        """#uppercased string"""
        self.assertEqual(max_integer("C IS FUN"), "U")
        """#upper and lowercased string"""
        self.assertEqual(max_integer("Teach Me PytHon"), "y")
        """#list of chars"""
        self.assertEqual(max_integer(['d', 's', 'm', 'z']), 'z')
        """#list of words"""
        self.assertEqual(max_integer(["this", "is", "fun"]), "this")
        """#array of chars"""
        self.assertEqual(max_integer(['d', 's', 'x', 'm', 'x', 'm']), 'x')

    def test_max_tuples(self):
        """test for tuples"""

        """#ordered tuple"""
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
        """#unordered tuple"""
        self.assertEqual(max_integer((1, 3, 4, 2)), 4)
        """#tuple with negative int"""
        self.assertEqual(max_integer((6, -3, 4, 2)), 6)
        """#empty tuple"""
        self.assertEqual(max_integer(()), None)

    def test_max_invalid(self):
        """Test for invalid argument"""

        """#test for integer"""
        self.assertRaises(TypeError, max_integer, 4)
        """ #test for None"""
        self.assertRaises(TypeError, max_integer, None)

        """#second method of asser raise(using context)"""
        with self.assertRaises(TypeError):
            max_integer(float('inf'))
