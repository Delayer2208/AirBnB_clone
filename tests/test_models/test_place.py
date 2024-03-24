import os
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    def test_place_instantiation_no_args(self):
        """Test instantiation of Place class with no arguments."""
        self.assertEqual(Place, type(Place()))

    def test_place_instance_stored_in_objects(self):
        """Test if new instance of Place is stored in the objects dictionary."""
        place_instance = Place()
        self.assertIn(place_instance, models.storage.all().values())


class TestPlaceSave(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up method to prepare for testing."""
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Clean up method after testing."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_save_updates_updated_at(self):
        """Test if the save method updates the updated_at attribute."""
        place_instance = Place()
        sleep(0.05)
        first_updated_at = place_instance.updated_at
        place_instance.save()
        self.assertLess(first_updated_at, place_instance.updated_at)


class TestPlaceToDict(unittest.TestCase):
    def test_to_dict_returns_dict(self):
        """Test if to_dict method returns a dictionary."""
        place_instance = Place()
        self.assertIsInstance(place_instance.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
