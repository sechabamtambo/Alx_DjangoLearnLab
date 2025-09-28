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

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'Book Two', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_delete_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'Updated', 'publication_year': 2000, 'author': self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])

        response = self.client.delete(self.delete_url)
        self.assertIn(response.status_code, [status.HTTP_204_NO_CONTENT, status.HTTP_200_OK])