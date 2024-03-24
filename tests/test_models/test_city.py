import os
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCityInstantiation(unittest.TestCase):
    def test_city_instantiation_no_args(self):
        """Test instantiation of City class with no arguments."""
        self.assertEqual(City, type(City()))

    def test_city_instance_stored_in_objects(self):
        """Test if new instance of City is stored in the objects dictionary."""
        city_instance = City()
        self.assertIn(city_instance, models.storage.all().values())


class TestCitySave(unittest.TestCase):
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
        city_instance = City()
        sleep(0.05)
        first_updated_at = city_instance.updated_at
        city_instance.save()
        self.assertLess(first_updated_at, city_instance.updated_at)


class TestCityToDict(unittest.TestCase):
    def test_to_dict_returns_dict(self):
        """Test if to_dict method returns a dictionary."""
        city_instance = City()
        self.assertIsInstance(city_instance.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
