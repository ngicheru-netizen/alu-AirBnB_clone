"""Tests for the model package."""

import unittest

from models.base_model import BaseModel
from models.user import User


class TestBaseModel(unittest.TestCase):
    """Test shared model behavior."""

    def test_model_has_id_and_timestamps(self):
        """A new model should have identity and timestamps."""
        model = BaseModel()

        self.assertIsInstance(model.id, str)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_to_dict_contains_class_name(self):
        """Serialized data should identify the model class."""
        data = User().to_dict()

        self.assertEqual(data["__class__"], "User")
        self.assertIsInstance(data["created_at"], str)


if __name__ == "__main__":
    unittest.main()
