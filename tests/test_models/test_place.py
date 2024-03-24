#!/usr/bin/env python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlaceInstantiation
    TestPlaceSave
    TestPlaceToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_class_attribute(self):
        place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(place
