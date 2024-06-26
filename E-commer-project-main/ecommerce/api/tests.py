from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .tasks import check_past_due_orders

User = get_user_model()


class UserRegistrationTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.login_url = reverse('user-login')
        self.user_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'password': 'securepassword'
        }

    def test_user_registration(self):
        response = self.client.post(
            self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        self.client.post(self.register_url, self.user_data, format='json')
        login_data = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)


class OrderAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            'testuser', 'test@example.com', 'testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_create_order(self):
        url = reverse('order-new')
        order_data = {
            'name': 'Test Product',
            'sku': 'SKU12345',
            'price': '99.99',
            'delivery_date': '01-01-2024'
        }
        response = self.client.post(url, order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.order_id = response.data["id"]

    def test_retrieve_order(self):
        url = reverse('order-new')
        order_data = {
            'name': 'Test Product',
            'sku': 'SKU12348',
            'price': '99.99',
            'delivery_date': '01-01-2024'
        }
        response = self.client.post(url, order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        order_id = response.data["id"]
        url = reverse('order-detail', args=[order_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], order_id)


class TaskTestCase(TestCase):

    def test_check_past_due_orders(self):
        result = check_past_due_orders.delay()
        self.assertTrue(result)
