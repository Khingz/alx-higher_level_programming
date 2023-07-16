#!/usr/bin/python3
"""unittest for base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase_Class_Instance(unittest.TestCase):
    """Test for class instantiation"""
    def test_unique_id(self):
        self.assertEqual(Base(34).id, 34)

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

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
           Base(2, 3, 5)

        with self.assertRaises(TypeError):
           Base(2, 3)

    def test_non_int_arg(self):
        self.assertEqual("python", Base("python").id)
        self.assertEqual(5.5, Base(5.5).id)
        self.assertEqual(complex(10), Base(complex(10)).id)
        self.assertEqual({"key": 12, "value": 34}, Base({"key": 12, "value": 34}).id)
        self.assertEqual(False, Base(False).id)
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)
        self.assertEqual((1, 2), Base((1, 2)).id)
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)
        self.assertEqual(range(5), Base(range(5)).id)
        self.assertEqual(bytearray(b'hello'), Base(bytearray(b'hello')).id)

    def test_nb_private(self):
        with self.assertRaises(AttributeError):
            print(Base(34).__nb_instances)


class TestBaseMethod_to_json_string(unittest.TestCase):
    """Test to string method"""
    def test_to_json_string_without_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], "hello")

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_type(self):
        rect = Rectangle(10, 7, 2, 8, 6)
        sq = Square(10, 2, 3, 4)
        rect = [rect.to_dictionary()]
        sq = [sq.to_dictionary()]
        self.assertEqual(str, type(Base.to_json_string(rect)))
        self.assertEqual(str, type(Base.to_json_string(sq)))

    def test_to_json_string_rectangle_dict(self):
        rect1 = Rectangle(10, 7, 2, 8, 23)
        rect2 = Rectangle(10, 7, 2, 8)
        self.assertTrue(len(Base.to_json_string([rect1.to_dictionary()])) == 54)
        rect_list = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(rect_list)) == 107)

    def test_to_json_string_square_dict(self):
        sq1 = Square(10, 2, 1)
        sq2 = Square(10, 2, 1, 12)
        self.assertTrue(len(Base.to_json_string([sq1.to_dictionary()])) == 39)
        sq_list = [sq1.to_dictionary(), sq2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string((sq_list))) == 79)


class TestBaseMethod_from_json_string(unittest.TestCase):
    """Test method for from_json_string"""
    def test_from_json_string_without_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        list_input2 = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

        json_list_input2 = Rectangle.to_json_string(list_input2)
        list_output2 = Rectangle.from_json_string(json_list_input2)
        self.assertEqual(list_input2, list_output2)

    def test_from_json_string_squares(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        list_input2 = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

        json_list_input2 = Rectangle.to_json_string(list_input2)
        list_output2 = Rectangle.from_json_string(json_list_input2)
        self.assertEqual(list_input2, list_output2)


class TestBaseMethod_create(unittest.TestCase):
    """Test create method of Base clss"""
    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_rectangle(self):
        sq1 = Square(7, 9, 1, 10)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual(str(sq1), "[Square] (10) 9/1 - 7")
        self.assertEqual(str(sq2), "[Square] (10) 9/1 - 7")
        self.assertIsNot(sq1, sq2)
        self.assertNotEqual(sq1, sq2)


class TestBaseMethod_save_to_file(unittest.TestCase):
    """Test for save to file method of base class"""
    @classmethod
    def tearDown(self):
        """Delete any created rectangle.jspn or square.json file"""
        try:
            os.remove("Base.json")
        except OSError:
            pass
        try:
            os.remove("Rectangle.json")
        except OSError:
            pass
        try:
            os.remove("Square.json")
        except OSError:
            pass

    def test_save_to_file_rectangle(self):
        rect = Rectangle(10, 7, 2, 8, 23)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 54)

        Rectangle.save_to_file([rect, rect2])
        with open("Rectangle.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 106)

    def test_save_to_file_square(self):
        sq = Square(10, 2, 1)
        sq2 = Square(10, 2, 1, 12)
        Square.save_to_file([sq])
        with open("Square.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 39)

        Square.save_to_file([sq, sq2])
        with open("Square.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 79)

    def test_save_to_file_cls_name_creation(self):
        rect = Rectangle(10, 7, 2, 8, 23)
        Base.save_to_file([rect])
        with open("Base.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 54)

    def test_save_to_file_multiple_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], [])

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_without_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()



if __name__ == "__main__":
    unittest.main()
