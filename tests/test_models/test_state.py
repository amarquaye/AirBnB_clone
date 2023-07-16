#!/usr/bin/python3
"""
This is the unittest for amenity.py
"""


import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ This tests instances and methods from State class """

    s = State()

    def test_class_exists(self):
        """This tests if class exists"""
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.s)), res)

    def test_user_inheritance(self):
        """To test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.s, State)

    def testHasAttributes(self):
        """To verify if attributes exist"""
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))

    def test_types(self):
        """And this tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime.datetime)
        self.assertIsInstance(self.s.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
