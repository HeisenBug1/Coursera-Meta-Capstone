from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from Restaurant.models import Menu, Booking
from Restaurant.serializers import MenuSerializer, BookingSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class IndexViewTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class MenuItemsViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item = Menu.objects.create(title="Pasta", price=12.99, inventory=100)

    def test_get_menu_items(self):
        response = self.client.get(reverse('menuitems-list'))
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_create_menu_item(self):
        data = {'title': 'Pizza', 'price': 9.99, 'inventory': 50}
        response = self.client.post(reverse('menuitems-list'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(Menu.objects.get(id=response.data['id']).title, 'Pizza')


class SingleMenuItemViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item = Menu.objects.create(title="Pasta", price=12.99, inventory=100)

    def test_get_single_menu_item(self):
        response = self.client.get(reverse('menuitem-detail', kwargs={'pk': self.menu_item.pk}))
        serializer = MenuSerializer(self.menu_item)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_update_menu_item(self):
        data = {'title': 'Spaghetti', 'price': 14.99, 'inventory': 80}
        response = self.client.put(reverse('menuitem-detail', kwargs={'pk': self.menu_item.pk}), data)
        self.menu_item.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.menu_item.title, 'Spaghetti')

    def test_delete_menu_item(self):
        response = self.client.delete(reverse('menuitem-detail', kwargs={'pk': self.menu_item.pk}))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Menu.objects.count(), 0)


class BookingViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.booking = Booking.objects.create(name="John Doe", no_of_guests=4, booking_date="2024-09-22T18:00:00Z")

    def test_get_bookings(self):
        response = self.client.get(reverse('booking-list'))
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_create_booking(self):
        data = {'name': 'Jane Doe', 'no_of_guests': 2, 'booking_date': '2024-09-23T18:00:00Z'}
        response = self.client.post(reverse('booking-list'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 2)
        self.assertEqual(Booking.objects.get(id=response.data['id']).name, 'Jane Doe')

    def test_update_booking(self):
        data = {'name': 'John Smith', 'no_of_guests': 5, 'booking_date': '2024-09-24T18:00:00Z'}
        response = self.client.put(reverse('booking-detail', kwargs={'pk': self.booking.pk}), data)
        self.booking.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.booking.name, 'John Smith')

    def test_delete_booking(self):
        response = self.client.delete(reverse('booking-detail', kwargs={'pk': self.booking.pk}))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Booking.objects.count(), 0)
