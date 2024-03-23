import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up test instances."""
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_unique_id(self):
        """Test if each instance has a unique ID."""
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_instance_type(self):
        """Test instance type."""
        self.assertIsInstance(self.model1, BaseModel)
        self.assertIsInstance(str(self.model1), str)

    def test_representation(self):
        """Test string representation."""
        representation = "[BaseModel] ({}) {}".format(
            self.model1.id, self.model1.__dict__)
        self.assertEqual(str(self.model1), representation)

    def test_to_dict(self):
        """Test conversion to dictionary."""
        self.assertIsInstance(self.model2.to_dict(), dict)

    def test_created_at_type(self):
        """Test type of created_at attribute."""
        self.assertIsInstance(self.model1.created_at, datetime)

    def test_updated_at_type(self):
        """Test type of updated_at attribute."""
        self.assertIsInstance(self.model1.updated_at, datetime)
