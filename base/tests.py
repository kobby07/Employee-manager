from urllib import response
from uuid import RESERVED_FUTURE
from django.test import TestCase, Client
from django.urls import reverse

class EmployeeTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
    
    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        
    def test_signup_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)