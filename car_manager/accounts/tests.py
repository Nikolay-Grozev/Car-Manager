from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test.client import Client


class UserRegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('create profile')
        self.user_data = {
            'username': 'test_user',
            'password1': 'test_password123',
            'password2': 'test_password123',

        }

    def test_user_registration(self):
        # Arrange: Prepare the data and environment
        initial_user_count = get_user_model().objects.count()

        # Act: Perform the action being tested
        response = self.client.post(self.register_url, self.user_data)

        # Assert: Check the results of the action
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home page'))
        self.assertEqual(get_user_model().objects.count(), initial_user_count + 1)

        # Additional assertions for logging in and user's profile page
        user = get_user_model().objects.get(username=self.user_data['username'])
        self.client.login(username=self.user_data['username'], password=self.user_data['password1'])
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)


class UserLoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = get_user_model().objects.create_user(username='test_user', password='test_password123')
        self.login_data = {
            'username': 'test_user',
            'password': 'test_password123',
        }

    def test_get_success_url(self):
        # Arrange: Prepare the data and environment

        # Act: Perform the action being tested
        response = self.client.post(self.login_url, self.login_data)

        # Assert: Check the results of the action
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home page'))
