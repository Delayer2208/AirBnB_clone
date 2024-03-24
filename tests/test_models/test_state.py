import os
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestStateInstantiation(unittest.TestCase):
    def test_state_instantiation_no_args(self):
        """Test instantiation of State class with no arguments."""
        self.assertEqual(State, type(State()))

    def test_state_instance_stored_in_objects(self):
        """Test if new instance of State is stored in the objects dictionary."""
        state_instance = State()
        self.assertIn(state_instance, models.storage.all().values())


class TestStateSave(unittest.TestCase):
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
        state_instance = State()
        sleep(0.05)
        first_updated_at = state_instance.updated_at
        state_instance.save()
        self.assertLess(first_updated_at, state_instance.updated_at)


class TestStateToDict(unittest.TestCase):
    def test_to_dict_returns_dict(self):
     
