from Order_Creation import Order
from unittest import TestCase


class TestOrder(TestCase):
    def test_get_id(self):
        # Create an instance of the Order class
        order = Order(1, "Wine", 5, "Pending")
        # Check that the getter returns the expected value
        self.assertEqual(order.get_id(), 1)

    def test_set_id(self):
        # Create an instance of the Order class
        order = Order(1, "Wine", 5, "Pending")
        # Modify the id attribute using the setter
        order.set_id(2)
        # Check that the value has been updated correctly
        self.assertEqual(order.get_id(), 2)

    def test_get_bottle_type(self):
        # Create an instance of the Order class
        order = Order(1, "Wine", 5, "Pending")
        # Check that the getter returns the expected value
        self.assertEqual(order.get_bottle_type(), "Wine")

    def test_set_bottle_type(self):
        # Create an instance of the Order class
        order = Order(1, "Wine", 5, "Pending")
        # Modify the bottle_type attribute using the setter
        order.set_bottle_type("Beer")
        # Check that the value has been updated correctly
        self.assertEqual(order.get_bottle_type(), "Beer")

    def test_get_quantity(self):
        # Create an instance of the Order class
        order = Order(1, "Wine", 5, "Pending")
        # Check that the getter returns the expected value
        self.assertEqual(order.get_quantity(), 5)

    def test_set_quantity(self):
        # Create an instance of the Order class
        order = Order(1, "Wine", 5, "Pending")
        # Modify the quantity attribute using the setter
        order.set_quantity(10)
        # Check that the value has been updated correctly
        self.assertEqual(order.get_quantity(), 10)

    def test_get_status(self):
        # Create an instance of the Order class
        order = Order(1, "Wine", 5, "Pending")
        # Check that the getter returns the expected value
        self.assertEqual(order.get_status(), "Pending")

    def test_set_status(self):
        # Create an instance of the Order class
        order = Order(1, "Wine", 5, "Pending")
        # Modify the status attribute using the setter
        order.set_status("Delivered")
        # Check that the value has been updated correctly
        self.assertEqual(order.get_status(), "Delivered")
