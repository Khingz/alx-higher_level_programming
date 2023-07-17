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
        self.assertEqual(
                {"key": 12, "value": 34},
                Base({"key": 12, "value": 34}).id
                )
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
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(1, 7, 2, 8)
        result = len(Base.to_json_string([rect1.to_dictionary()]))
        self.assertTrue(result == 53)
        rect_list = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(rect_list)) == 106)

    def test_to_json_string_square_dict(self):
        sq1 = Square(10, 2, 1, 9)
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
                {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3}
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
        sq = Square(10, 7, 2, 8)
        sq2 = Square(8, 1, 2, 3)
        Square.save_to_file([sq])
        with open("Square.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 39)

        Square.save_to_file([sq, sq2])
        with open("Square.json", "r") as fd:
            self.assertTrue(len(fd.read()) == 77)

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


class TestBaseMethod_load_from_file(unittest.TestCase):
    """Test for load from file function"""
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

    def test_load_from_file_rectangle(self):
        rect = Rectangle(10, 7, 2, 8, 23)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect), str(list_rectangles_output[0]))
        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_from_file_rectnagle_type(self):
        rect = Rectangle(10, 7, 2, 8, 23)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect, rect2])
        list_o = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in list_o))

    def test_load_from_file_square(self):
        sq = Square(10, 2, 1)
        sq2 = Square(10, 2, 1, 12)
        Square.save_to_file([sq, sq2])
        list_o = Square.load_from_file()
        self.assertEqual(str(sq), str(list_o[0]))
        self.assertEqual(str(sq2), str(list_o[1]))

    def test_load_from_file_square_type(self):
        sq = Square(10, 2, 1)
        sq2 = Square(10, 2, 1, 12)
        Square.save_to_file([sq, sq2])
        list_o = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in list_o))

    def test_load_from_file_no_file(self):
        list_o = Square.load_from_file()
        self.assertEqual([], list_o)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], [])


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

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

    def test_save_to_file_csv_rectangle(self):
        rect = Rectangle(10, 2, 5, 4, 6)
        Rectangle.save_to_file_csv([rect])
        with open("Rectangle.csv", "r") as fd:
            self.assertTrue("10,2,5,4,6", fd.read())

        rect2 = Rectangle(2, 7, 3, 6, 4)
        Rectangle.save_to_file_csv([rect, rect2])
        result = "10,2,5,4,6\n2,7,3,6,4"
        with open("Rectangle.csv", "r") as fd:
            self.assertTrue(result, fd.read())

    def test_save_to_file_csv_one_square(self):
        sq = Square(3, 9, 2, 4)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as f:
            self.assertTrue("3,9,2,4", f.read())

        sq2 = Square(2, 1, 5, 3)
        Square.save_to_file_csv([sq, sq2])
        result = "3,9,2,4\n2,1,5,3"
        with open("Square.csv", "r") as fd:
            self.assertTrue(result, fd.read())

    def test_save_to_file_cls_name_creation(self):
        sq = Square(3, 9, 2, 4)
        Base.save_to_file_csv([sq])
        with open("Base.csv", "r") as f:
            self.assertTrue("3,9,2,4", f.read())

    def test_save_to_file_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_without_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], [])


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """
    Test for laod from
    """
    @classmethod
    def tearDown(self):
        try:
            os.remove("Base.csv")
        except OSError:
            pass
        try:
            os.remove("Rectangle.csv")
        except OSError:
            pass
        try:
            os.remove("Square.csv")
        except OSError:
            pass

    def test_load_from_file_csv_no_file(self):
        output = Rectangle.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_rectangle(self):
        rect = Rectangle(10, 2, 5, 4, 6)
        rect2 = Rectangle(2, 7, 3, 6, 4)
        Rectangle.save_to_file_csv([rect, rect2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect), str(list_rectangles_output[0]))

        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        rect = Rectangle(10, 2, 5, 4, 6)
        rect2 = Rectangle(2, 7, 3, 6, 4)
        Rectangle.save_to_file_csv([rect, rect2])
        l_out = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in l_out))

    def test_load_from_file_csv_square(self):
        sq = Square(3, 9, 2, 4)
        sq2 = Square(2, 1, 5, 3)
        Square.save_to_file_csv([sq, sq2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sq), str(list_squares_output[0]))
        self.assertEqual(str(sq2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        sq = Square(3, 9, 2, 4)
        sq2 = Square(2, 1, 5, 3)
        Square.save_to_file_csv([sq, sq2])
        l_out = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in l_out))

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], [])


if __name__ == "__main__":
    unittest.main()
