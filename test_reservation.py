"""
Unit tests for Reservation class.
"""
import unittest
import os
from reservation import Reservation
from customer import Customer
from hotel import Hotel


class TestReservation(unittest.TestCase):
    """Test cases for Reservation class."""

    def setUp(self):
        """Clean up and set up initial state."""
        Files = [Reservation.FILE_NAME, Customer.FILE_NAME, Hotel.FILE_NAME]
        for f in Files:
            if os.path.exists(f):
                os.remove(f)
        # Create a customer and a hotel for testing
        Customer.create_customer("C1", "John Doe", "john@example.com")
        Hotel.create_hotel("H1", "Grand Hotel", "City A", 1)

    def tearDown(self):
        """Clean up after tests."""
        Files = [Reservation.FILE_NAME, Customer.FILE_NAME, Hotel.FILE_NAME]
        for f in Files:
            if os.path.exists(f):
                os.remove(f)

    def test_create_reservation(self):
        """Test creating a reservation."""
        self.assertTrue(Reservation.create_reservation("R1", "C1", "H1"))
        reservations = Reservation.load_reservations()
        self.assertEqual(len(reservations), 1)
        # Check if room count decreased
        hotel = Hotel.display_hotel("H1")
        self.assertEqual(hotel["rooms"], 0)

    def test_create_reservation_no_rooms(self):
        """Test creating a reservation when no rooms are available (Negative)."""
        Reservation.create_reservation("R1", "C1", "H1")
        # Try second reservation in same hotel (only 1 room available initially)
        Customer.create_customer("C2", "Jane", "jane@example.com")
        self.assertFalse(Reservation.create_reservation("R2", "C2", "H1"))

    def test_create_reservation_invalid_customer(self):
        """Test creating a reservation with non-existent customer (Negative)."""
        self.assertFalse(Reservation.create_reservation("R1", "INVALID", "H1"))

    def test_create_reservation_invalid_hotel(self):
        """Test creating a reservation with non-existent hotel (Negative)."""
        self.assertFalse(Reservation.create_reservation("R1", "C1", "INVALID"))

    def test_cancel_reservation(self):
        """Test cancelling a reservation."""
        Reservation.create_reservation("R1", "C1", "H1")
        self.assertTrue(Reservation.cancel_reservation("R1"))
        self.assertEqual(len(Reservation.load_reservations()), 0)
        # Check if room count increased
        hotel = Hotel.display_hotel("H1")
        self.assertEqual(hotel["rooms"], 1)

    def test_cancel_non_existent_reservation(self):
        """Test cancelling a non-existent reservation (Negative)."""
        self.assertFalse(Reservation.cancel_reservation("NON_EXISTENT"))


if __name__ == "__main__":
    unittest.main()
