"""
Unit tests for Hotel class.
"""
import unittest
import os
from hotel import Hotel


class TestHotel(unittest.TestCase):
    """Test cases for Hotel class."""

    def setUp(self):
        """Clean up and set up initial state."""
        if os.path.exists(Hotel.FILE_NAME):
            os.remove(Hotel.FILE_NAME)

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(Hotel.FILE_NAME):
            os.remove(Hotel.FILE_NAME)

    def test_create_hotel(self):
        """Test creating a hotel."""
        self.assertTrue(Hotel.create_hotel("H1", "Grand Hotel", "City A", 10))
        hotels = Hotel.load_hotels()
        self.assertEqual(len(hotels), 1)

    def test_create_duplicate_hotel(self):
        """Test creating a hotel with existing ID (Negative)."""
        Hotel.create_hotel("H1", "Grand Hotel", "City A", 10)
        self.assertFalse(Hotel.create_hotel("H1", "Other", "City B", 5))

    def test_delete_hotel(self):
        """Test deleting a hotel."""
        Hotel.create_hotel("H1", "Grand Hotel", "City A", 10)
        self.assertTrue(Hotel.delete_hotel("H1"))

    def test_delete_non_existent_hotel(self):
        """Test deleting a non-existent hotel (Negative)."""
        self.assertFalse(Hotel.delete_hotel("NON_EXISTENT"))

    def test_display_hotel(self):
        """Test displaying a hotel."""
        Hotel.create_hotel("H1", "Grand Hotel", "City A", 10)
        hotel = Hotel.display_hotel("H1")
        self.assertIsNotNone(hotel)

    def test_modify_hotel(self):
        """Test modifying a hotel."""
        Hotel.create_hotel("H1", "Grand Hotel", "City A", 10)
        self.assertTrue(Hotel.modify_hotel("H1", rooms=5))
        hotel = Hotel.display_hotel("H1")
        self.assertEqual(hotel["rooms"], 5)


if __name__ == "__main__":
    unittest.main()
