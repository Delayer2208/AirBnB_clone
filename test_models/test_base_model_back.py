import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up test instances."""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down method."""
        del self.model

    def test_id_type(self):
        """Test the type and format of the ID."""
        self.assertTrue(isinstance(self.model.id, str))
        self.assertTrue(uuid.UUID(self.model.id))

    def test_created_at(self):
        """Test the creation time."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(now, self.model.created_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test the update time."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(now, self.model.updated_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_format(self):
        """Test the string representation."""
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected)

    def test_str_after_update(self):
        """Test string representation after updating."""
        self.model.name = "test_name"
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected)

    def test_save_updates(self):
        """Test if save method updates attributes."""
        self.model.save()
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected)

    def test_to_dict_format(self):
        """Test the format of the dictionary representation."""
        my_dict = self.model.to_dict()
        self.assertIn("id", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("__class__", my_dict)

    def test_to_dict_attributes(self):
        """Test the attributes in the dictionary representation."""
        my_dict = self.model.to_dict()
        self.assertEqual(my_dict["id"], self.model.id)
        self.assertEqual(my_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"], self.model.updated_at.isoformat())
        self.assertEqual(my_dict["__class__"], "BaseModel")

    def test_to_dict_after_update(self):
        """Test dictionary representation after updating."""
        self.model.name = "test_name"
        my_dict = self.model.to_dict()
        self.assertEqual(my_dict["name"], "test_name")

    def test_save_updates_to_dict(self):
        """Test if calling save method updates dictionary."""
        self.model.save()
        my_dict = self.model.to_dict()
        self.assertEqual(my_dict["updated_at"], self.model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
