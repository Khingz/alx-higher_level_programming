#!/usr/bin/python3
"""unittest for base class"""
import unittest
from models.base import Base


class Test_Class_Instance(unittest.TestCase):
    """Test for class instantiation"""
    def test_unique_id(self):
        a = Base(34)
        self.assertEqual(a.id, 34)

    def test_consistent_id(self):
        a = Base()
        b = Base()
        c = Base(15)
        d = Base()
        e = Base()
        f = Base()
        self.assertEqual(a.id, b.id - 1)
        self.assertEqual(d.id, e.id - 1)
        self.assertEqual(d.id, f.id - 2)


if __name__ == "__main__":
    unittest.main()
