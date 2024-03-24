import os
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    def test_review_instantiation_no_args(self):
        """Test instantiation of Review class with no arguments."""
        self.assertEqual(Review, type(Review()))

    def test_review_instance_stored_in_objects(self):
        """Test if new instance of Review is stored in the objects dictionary."""
        review_instance = Review()
        self.assertIn(review_instance, models.storage.all().values())


class TestReviewSave(unittest.TestCase):
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
     
