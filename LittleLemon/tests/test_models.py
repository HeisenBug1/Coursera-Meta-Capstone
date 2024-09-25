from django.test import TestCase
from Restaurant.models import Booking, Menu
from datetime import datetime

class BookingModelTestCase(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=datetime(2024, 9, 22, 18, 0)
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.name, "John Doe")
        self.assertEqual(self.booking.no_of_guests, 4)
        self.assertEqual(self.booking.booking_date, datetime(2024, 9, 22, 18, 0))

    def test_booking_str(self):
        self.assertEqual(str(self.booking), "John Doe - 2024-09-22 18:00:00")

    
class MenuModelTestCase(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Pasta",
            price=12.99,
            inventory=100
        )

    def test_menu_creation(self):
        self.assertEqual(self.menu_item.title, "Pasta")
        self.assertEqual(self.menu_item.price, 12.99)
        self.assertEqual(self.menu_item.inventory, 100)

    def test_menu_str(self):
        self.assertEqual(str(self.menu_item), "Pasta : 12.99")
