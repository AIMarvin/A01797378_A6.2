"""
Module for Reservation management.
"""
from customer import Customer
from hotel import Hotel
from data_utils import DataHandler


class Reservation:
    """
    Class to manage reservation information and persistence.
    """
    FILE_NAME = "reservations.json"

    def __init__(self, reservation_id, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Convert reservation object to dictionary."""
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id
        }

    @classmethod
    def load_reservations(cls):
        """Load reservations from JSON file using DataHandler."""
        return DataHandler.load_data(cls.FILE_NAME)

    @classmethod
    def save_reservations(cls, reservations):
        """Save reservations list to JSON file using DataHandler."""
        DataHandler.save_data(cls.FILE_NAME, reservations)

    @classmethod
    def create_reservation(cls, reservation_id, customer_id, hotel_id):
        """Create a new reservation if customer and hotel exist."""
        customers = Customer.load_customers()
        if not any(c['customer_id'] == customer_id for c in customers):
            print(f"Customer with ID {customer_id} not found.")
            return False

        hotels = Hotel.load_hotels()
        hotel = next((h for h in hotels if h['hotel_id'] == hotel_id), None)
        if not hotel:
            print(f"Hotel with ID {hotel_id} not found.")
            return False

        if hotel['rooms'] <= 0:
            print(f"No rooms available in hotel {hotel_id}.")
            return False

        reservations = cls.load_reservations()
        if any(r['reservation_id'] == reservation_id for r in reservations):
            print(f"Reservation with ID {reservation_id} already exists.")
            return False

        new_reservation = cls(reservation_id, customer_id, hotel_id)
        reservations.append(new_reservation.to_dict())
        cls.save_reservations(reservations)

        Hotel.modify_hotel(hotel_id, rooms=hotel['rooms'] - 1)
        return True

    @classmethod
    def cancel_reservation(cls, reservation_id):
        """Cancel a reservation and release the room."""
        reservations = cls.load_reservations()
        reservation = next((r for r in reservations
                            if r['reservation_id'] == reservation_id), None)

        if not reservation:
            print(f"Reservation with ID {reservation_id} not found.")
            return False

        new_res = [r for r in reservations
                   if r['reservation_id'] != reservation_id]
        cls.save_reservations(new_res)

        hotels = Hotel.load_hotels()
        hotel = next((h for h in hotels
                      if h['hotel_id'] == reservation['hotel_id']), None)
        if hotel:
            Hotel.modify_hotel(hotel['hotel_id'], rooms=hotel['rooms'] + 1)

        return True
