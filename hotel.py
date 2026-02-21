"""
Module for Hotel management.
"""
from data_utils import DataHandler


class Hotel:
    """
    Class to manage hotel information and persistence.
    """
    FILE_NAME = "hotels.json"

    def __init__(self, hotel_id, name, location, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    def to_dict(self):
        """Convert hotel object to dictionary."""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms
        }

    @classmethod
    def load_hotels(cls):
        """Load hotels from JSON file using DataHandler."""
        return DataHandler.load_data(cls.FILE_NAME)

    @classmethod
    def save_hotels(cls, hotels):
        """Save hotels list to JSON file using DataHandler."""
        DataHandler.save_data(cls.FILE_NAME, hotels)

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms):
        """Create a new hotel and save it."""
        hotels = cls.load_hotels()
        if any(h['hotel_id'] == hotel_id for h in hotels):
            print(f"Hotel with ID {hotel_id} already exists.")
            return False
        new_hotel = cls(hotel_id, name, location, rooms)
        hotels.append(new_hotel.to_dict())
        cls.save_hotels(hotels)
        return True

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Delete a hotel by ID."""
        hotels = cls.load_hotels()
        new_hotels = [h for h in hotels if h['hotel_id'] != hotel_id]
        if len(new_hotels) == len(hotels):
            print(f"Hotel with ID {hotel_id} not found.")
            return False
        cls.save_hotels(new_hotels)
        return True

    @classmethod
    def display_hotel(cls, hotel_id):
        """Display hotel information."""
        hotels = cls.load_hotels()
        hotel = next((h for h in hotels if h['hotel_id'] == hotel_id), None)
        if hotel:
            print(f"Hotel ID: {hotel['hotel_id']}")
            print(f"Name: {hotel['name']}")
            print(f"Location: {hotel['location']}")
            print(f"Rooms available: {hotel['rooms']}")
            return hotel
        print(f"Hotel with ID {hotel_id} not found.")
        return None

    @classmethod
    def modify_hotel(cls, hotel_id, name=None, location=None, rooms=None):
        """Modify hotel information."""
        hotels = cls.load_hotels()
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                if name:
                    hotel['name'] = name
                if location:
                    hotel['location'] = location
                if rooms is not None:
                    hotel['rooms'] = rooms
                cls.save_hotels(hotels)
                return True
        print(f"Hotel with ID {hotel_id} not found.")
        return False
