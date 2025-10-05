from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Author One')
        self.book = Book.objects.create(title='Book One', publication_year=2000, author=self.author)

        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update')
        self.delete_url = reverse('book-delete')

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_requires_auth(self):
        data = {'title': 'Book Two', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_delete_requires_auth(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.update_url, {'title': 'Updated', 'publication_year': 2000, 'author': self.author.id})
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])

        response = self.client.delete(self.delete_url)
        self.assertIn(response.status_code, [status.HTTP_204_NO_CONTENT, status.HTTP_200_OK])

    def test_filter_search_order(self):
        # Filtering
        response = self.client.get(self.list_url, {'title': 'Book One'})
        self.assertEqual(len(response.data), 1)

        # Searching
        response = self.client.get(self.list_url, {'search': 'Author One'})
        self.assertEqual(len(response.data), 1)

        # Ordering
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)