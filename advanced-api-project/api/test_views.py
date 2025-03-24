# api/test_views.py
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from api.models import Book  # Assuming your Book model is in api/models.py

class BookCreateTest(TestCase):
    def setUp(self):
        # This runs before each test method
        self.client = APIClient()
        self.create_url = reverse('book-list')  # Assuming you have a URL named 'book-list' for creating books

    def test_can_create_book(self):
        # What data are we going to send to create a book?
        book_data = {'title': 'The Hitchhiker\'s Guide to the Galaxy', 'author': 'Douglas Adams', 'publication_date': '1979-10-12'}

        # Simulate making a POST request to our create book endpoint
        response = self.client.post(self.create_url, book_data, format='json')

        # Now we check if the response is what we expect

        # Check if the status code is 201 (Created) - this means the book was successfully created
        self.assertEqual(response.status_code, 201)

        # Check if the book was actually saved in the database
        self.assertEqual(Book.objects.count(), 1)

        # Check if the data in the response matches what we sent
        self.assertEqual(response.data['title'], 'The Hitchhiker\'s Guide to the Galaxy')
        self.assertEqual(response.data['author'], 'Douglas Adams')
        self.assertEqual(response.data['publication_date'], '1979-10-12')
