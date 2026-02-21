"""
Module for Customer management.
"""
from data_utils import DataHandler


class Customer:
    """
    Class to manage customer information and persistence.
    """
    FILE_NAME = "customers.json"

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert customer object to dictionary."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }

    @classmethod
    def load_customers(cls):
        """Load customers from JSON file using DataHandler."""
        return DataHandler.load_data(cls.FILE_NAME)

    @classmethod
    def save_customers(cls, customers):
        """Save customers list to JSON file using DataHandler."""
        DataHandler.save_data(cls.FILE_NAME, customers)

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """Create a new customer and save it."""
        customers = cls.load_customers()
        if any(c['customer_id'] == customer_id for c in customers):
            print(f"Customer with ID {customer_id} already exists.")
            return False
        new_customer = cls(customer_id, name, email)
        customers.append(new_customer.to_dict())
        cls.save_customers(customers)
        return True

    @classmethod
    def delete_customer(cls, customer_id):
        """Delete a customer by ID."""
        customers = cls.load_customers()
        new_customers = [c for c in customers if c['customer_id'] != customer_id]
        if len(new_customers) == len(customers):
            print(f"Customer with ID {customer_id} not found.")
            return False
        cls.save_customers(new_customers)
        return True

    @classmethod
    def display_customer(cls, customer_id):
        """Display customer information."""
        customers = cls.load_customers()
        customer = next((c for c in customers
                         if c['customer_id'] == customer_id),
                        None)
        if customer:
            print(f"Customer ID: {customer['customer_id']}")
            print(f"Name: {customer['name']}")
            print(f"Email: {customer['email']}")
            return customer
        print(f"Customer with ID {customer_id} not found.")
        return None

    @classmethod
    def modify_customer(cls, customer_id, name=None, email=None):
        """Modify customer information."""
        customers = cls.load_customers()
        for customer in customers:
            if customer['customer_id'] == customer_id:
                if name:
                    customer['name'] = name
                if email:
                    customer['email'] = email
                cls.save_customers(customers)
                return True
        print(f"Customer with ID {customer_id} not found.")
        return False
