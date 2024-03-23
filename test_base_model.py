from models.base_model import BaseModel
import json
import unittest

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_create_instance(self):
        """Test creating a new instance of BaseModel."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_attributes(self):
        """Test setting and accessing attributes."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My_First_Model")
        self.assertEqual(my_model.my_number, 89)

    def test_id_generation(self):
        """Test UUID generation."""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_to_dict_conversion(self):
        """Test conversion to dictionary."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json, dict)
        self.assertIn("id", my_model_json)
        self.assertIn("created_at", my_model_json)
        self.assertIn("updated_at", my_model_json)
        self.assertIn("__class__", my_model_json)
        self.assertEqual(my_model_json["name"], "My_First_Model")
        self.assertEqual(my_model_json["my_number"], 89)

    def test_json_serialization(self):
        """Test JSON serialization."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        serialized_json = json.dumps(my_model_json)
        self.assertIsInstance(serialized_json, str)

    def test_create_from_json(self):
        """Test creating an instance from JSON."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, new_model.id)
        self.assertEqual(my_model.name, new_model.name)
        self.assertEqual(my_model.my_number, new_model.my_number)

    def test_created_at_type(self):
        """Test created_at attribute type."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_str_representation(self):
        """Test string representation."""
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

if __name__ == "__main__":
    unittest.main()
