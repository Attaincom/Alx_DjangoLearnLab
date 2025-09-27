from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authenticated requests
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Create an author
        self.author = Author.objects.create(name="Chinua Achebe")
        
        # Create a book
        self.book = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Things Fall Apart")

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Things Fall Apart")

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {"title": "No Longer at Ease", "publication_year": 1960, "author": self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Should fail

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-create')
        data = {"title": "No Longer at Ease", "publication_year": 1960, "author": self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, "No Longer at Ease")

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update')
        data = {"title": "Updated Title", "publication_year": 1958, "author": self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
