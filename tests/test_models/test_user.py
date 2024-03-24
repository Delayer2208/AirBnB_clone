import os
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    def test_user_instantiation_no_args(self):
        """Test instantiation of User class with no arguments."""
        self.assertEqual(User, type(User()))

    def test_user_instance_stored_in_objects(self):
        """Test if new instance of User is stored in the objects dictionary."""
        user_instance = User()
        self.assertIn(user_instance, models.storage.all().values())


class TestUserSave(unittest.TestCase):
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
        user_instance = User()
        sleep(0.05)
        first_updated_at = user_instance.updated_at
        user_instance.save()
        self.assertLess(first_updated_at, user_instance.updated_at)


class TestUserToDict(unittest.TestCase):
    def test_to_dict_returns_dict(self):
        """Test if to_dict method returns a dictionary."""
        user_instance = User()
        self.assertIsInstance(user_instance.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
