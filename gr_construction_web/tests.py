from django.test import TestCase
from django.db import transaction
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Client


# Create your tests here.
class RegistrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='nullUser777', password='GoodMBadJ367')

    @transaction.atomic
    def test_create_client(self):
        self.client.logout()
        self.client.login(username='nullUser777', password='GoodMBadJ367')

        create_client_url = reverse('add-client')
        client_data = {
            'name': 'Jerry Doe',
            'status': 'Active',
            'email': 'jerry@example.com',
            'phone_number': '1234567890',
            'description': 'Test Client Created Successfully',
        }
        response = self.client.post(create_client_url, client_data)
        print(response)
        self.assertEqual(response.status_code, 200)
        new_client = Client.objects.filter(name='Jerry Doe').first()
        print("Test Client:", new_client)
        print("Test Client Status:", new_client.status if new_client else None)
        print("Test Client Email:", new_client.email if new_client else None)
        print("Test Client Number:", new_client.phone_number if new_client else None)
        print("Test Client Description:", new_client.description if new_client else None)
        self.assertIsNotNone(new_client)
        self.assertEqual(new_client.status, 'Active')
