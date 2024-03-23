import unittest
from models import storage
from models.base_model import BaseModel

class TestSaveReloadBaseModel(unittest.TestCase):
    """Test case for saving and reloading BaseModel instances."""

    def test_reload_objects(self):
        """Test reloading objects from storage."""
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertIsInstance(obj, BaseModel)

    def test_create_and_save_object(self):
        """Test creating and saving a new BaseModel instance."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(hasattr(my_model, 'id'))

        # Retrieve the object from storage
        retrieved_obj = storage.all()["BaseModel.{}".format(my_model.id)]
        self.assertIsInstance(retrieved_obj, BaseModel)
        self.assertEqual(retrieved_obj.name, "My_First_Model")
        self.assertEqual(retrieved_obj.my_number, 89)

if __name__ == "__main__":
    unittest.main()
