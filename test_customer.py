"""
Unit tests for Customer class.
"""
import unittest
import os
from customer import Customer


class TestCustomer(unittest.TestCase):
    """Test cases for Customer class."""

    def setUp(self):
        """Clean up and set up initial state."""
        if os.path.exists(Customer.FILE_NAME):
            os.remove(Customer.FILE_NAME)

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(Customer.FILE_NAME):
            os.remove(Customer.FILE_NAME)

    def test_create_customer(self):
        """Test creating a customer."""
        self.assertTrue(Customer.create_customer("C1", "John Doe",
                                                 "john@example.com"))
        customers = Customer.load_customers()
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0]["name"], "John Doe")

    def test_create_duplicate_customer(self):
        """Test creating a customer with existing ID (Negative)."""
        Customer.create_customer("C1", "John Doe", "john@example.com")
        self.assertFalse(Customer.create_customer("C1", "Jane Smith",
                                                  "jane@example.com"))

    def test_delete_customer(self):
        """Test deleting a customer."""
        Customer.create_customer("C1", "John Doe", "john@example.com")
        self.assertTrue(Customer.delete_customer("C1"))
        self.assertEqual(len(Customer.load_customers()), 0)

    def test_delete_non_existent_customer(self):
        """Test deleting a customer that doesn't exist (Negative)."""
        self.assertFalse(Customer.delete_customer("NON_EXISTENT"))

    def test_display_customer(self):
        """Test displaying a customer."""
        Customer.create_customer("C1", "John Doe", "john@example.com")
        customer = Customer.display_customer("C1")
        self.assertIsNotNone(customer)
        self.assertEqual(customer["name"], "John Doe")

    def test_display_non_existent_customer(self):
        """Test displaying a non-existent customer (Negative)."""
        self.assertIsNone(Customer.display_customer("NON_EXISTENT"))

    def test_modify_customer(self):
        """Test modifying a customer."""
        Customer.create_customer("C1", "John Doe", "john@example.com")
        self.assertTrue(Customer.modify_customer("C1", name="John Smith"))
        customer = Customer.display_customer("C1")
        self.assertEqual(customer["name"], "John Smith")

    def test_modify_non_existent_customer(self):
        """Test modifying a non-existent customer (Negative)."""
        self.assertFalse(Customer.modify_customer("NON_EXISTENT", name="None"))

    def test_load_malformed_json(self):
        """Test loading from a malformed JSON file (Negative)."""
        with open(Customer.FILE_NAME, 'w', encoding='utf-8') as file:
            file.write("INVALID JSON")
        self.assertEqual(Customer.load_customers(), [])


if __name__ == "__main__":
    unittest.main()
