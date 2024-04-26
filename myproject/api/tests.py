from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

class UserRegistrationTestCase(APITestCase):
    def test_user_registration(self):
        data = {"username": "testuser", "email": "test@example.com", "password": "securepassword123"}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)