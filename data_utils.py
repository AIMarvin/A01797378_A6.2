"""
Utility module for JSON data persistence.
"""
import json
import os


class DataHandler:
    """
    Handles loading and saving data to JSON files.
    """

    @staticmethod
    def load_data(file_name):
        """Load data from a JSON file."""
        if not os.path.exists(file_name):
            return []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    @staticmethod
    def save_data(file_name, data):
        """Save data to a JSON file."""
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            return True
        except IOError as error:
            print(f"Error saving data to {file_name}: {error}")
            return False
