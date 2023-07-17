#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests  class"""

    def setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Cleans up ."""
        pass

    def test_A_nb_objects_private(self):
        """Tests if nb_objects is private class attribute."""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        """Tests  initializes zero."""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        """Tests Base() instantiation."""
        bnx = Base()
        self.assertEqual(str(type(bnx)), "<class 'models.base.Base'>")
        self.assertEqual(bnx.__dict__, {"id": 1})
        self.assertEqual(bnx.id, 1)

    def test_D_constructor(self):
        """Tests signature."""
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        m = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), m)

    def test_D_constructor_args_2(self):
        """Tests constructor args."""
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        m = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), m)

    def test_E_consecutive_ids(self):
        """Tests ids."""
        bnx1 = Base()
        bnx2 = Base()
        self.assertEqual(bnx1.id + 1, bnx2.id)

    def test_F_id_synced(self):
        """Tests sync between class and instance id."""
        bnx = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), bnx.id)

    def test_F_id_synced_more(self):
        """Tests sync between class and instance id."""
        bnx = Base()
        bnx = Base("Foo")
        bnx = Base(98)
        bnx = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), bnx.id)

    def test_G_custom_id_int(self):
        """Tests custom id."""
        inx = 98
        bnx = Base(inx)
        self.assertEqual(bnx.id, inx)

    def test_G_custom_id_str(self):
        """Tests custom id."""
        inx = "FooBar"
        bnx = Base(inx)
        self.assertEqual(bnx.id, inx)

    def test_G_id_keyword(self):
        """Tests id passed as  arg."""
        inx = 421
        bnx = Base(id=inx)
        self.assertEqual(bnx.id, inx)
