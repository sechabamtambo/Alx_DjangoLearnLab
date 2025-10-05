from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="testpass123")
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", publication_year=2001, author=self.author)
        self.book_url = reverse("book-list")
        self.book_detail_url = reverse("book-detail", kwargs={"pk": self.book.id})

    def test_list_books(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        self.client.login(username="tester", password="testpass123")
        response = self.client.post(self.book_url, {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        response = self.client.post(self.book_url, {
            "title": "Unauthorized Book",
            "publication_year": 2022,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username="tester", password="testpass123")
        response = self.client.put(self.book_detail_url, {
            "title": "Updated Title",
            "publication_year": 2005,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        self.client.login(username="tester", password="testpass123")
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)