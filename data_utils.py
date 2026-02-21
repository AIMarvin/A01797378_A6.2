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
        """Load data from a JSON file. Prints error if malformed."""
        if not os.path.exists(file_name):
            return []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as error:
            print(f"Error loading {file_name}: {error}")
            return []

    @staticmethod
    def save_data(file_name, data):
        """Save data to a JSON file."""
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            return True
        except IOError as error:
            print(f"Error saving {file_name}: {error}")
            return False
