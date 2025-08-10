from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from .models import Book
from rest_framework import status
from django.urls import reverse
from unittest.mock import patch
from unittest.mock import MagicMock

class BookAPITests(APITestCase):
    """
    Tests for the Book model API endpoints.
    
    This class uses Django's APITestCase to simulate HTTP requests to the API.
    We'll test CRUD operations, filtering, ordering, and authentication/permissions.
    """
    def setUp(self):
        """
        Set up test data and client for each test.
        """
        global mock_db, book_counter
        mock_db.clear()
        book_counter = 1

        # Create a regular user and a superuser
        self.user1 = Book.objects.create_user(username='user1', password='password1')
        self.user2 = Book.objects.create_user(username='user2', password='password2')
        self.superuser = Book.objects.create_superuser(username='superuser', password='password3')

        # Create some sample books owned by different users
        self.book1 = Book(pk=1, title='The Catcher in the Rye', author='J.D. Salinger', publication_year=1951, user_id=self.user1.id)
        self.book2 = Book(pk=2, title='To Kill a Mockingbird', author='Harper Lee', publication_year=1960, user_id=self.user2.id)
        self.book3 = Book(pk=3, title='1984', author='George Orwell', publication_year=1949, user_id=self.user1.id)
        mock_db[1] = self.book1
        mock_db[2] = self.book2
        mock_db[3] = self.book3

        # Define the URL patterns for our endpoints
        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])

        # We'll use mock for our views to control their behavior
        self.book_list_view = MagicMock()
        self.book_detail_view = MagicMock()

        # Patch the views to use our mocks during testing
        patcher_list = patch('book_app.views.BookListCreateAPIView.as_view', return_value=self.mock_list_view)
        patcher_detail = patch('book_app.views.BookRetrieveUpdateDestroyAPIView.as_view', return_value=self.mock_detail_view)
        patcher_list.start()
        patcher_detail.start()
        self.addCleanup(patcher_list.stop)
        self.addCleanup(patcher_detail.stop)

        # Set up mock view behavior
        self.mock_list_view.return_value = self.client.get(self.list_url)
        self.mock_detail_view.return_value = self.client.get(self.detail_url(1))


    def test_book_create_authenticated_user(self):
        """
        Ensure an authenticated user can create a new book.
        """
        self.client.force_login(self.user1)
        data = {
            'title': 'Dune',
            'author': 'Frank Herbert',
            'publication_year': 1965
        }
        response = self.client.post(self.list_url, data, format='json')

        # Assert a 201 Created status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assert the response data is correct
        self.assertEqual(response.data['title'], 'Dune')
        self.assertEqual(response.data['author'], 'Frank Herbert')
        self.assertEqual(response.data['user'], self.user1.id)
        # Assert a new book was created in the mock database
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.get(pk=4).title, 'Dune')

    def test_book_create_unauthenticated_user(self):
        """
        Ensure an unauthenticated user cannot create a new book.
        """
        data = {
            'title': 'Foundation',
            'author': 'Isaac Asimov',
            'publication_year': 1951
        }
        response = self.client.post(self.list_url, data, format='json')

        # Assert a 401 Unauthorized status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # Assert no new book was created
        self.assertEqual(Book.objects.count(), 3)

    def test_book_update_by_owner(self):
        """
        Ensure the book's owner can update the book.
        """
        self.client.force_login(self.user1)
        updated_data = {
            'title': 'The Catcher in the Rye (Updated)',
            'author': 'J.D. Salinger',
            'publication_year': 1951
        }
        response = self.client.put(self.detail_url(self.book1.pk), updated_data, format='json')

        # Assert a 200 OK status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert the response data is updated
        self.assertEqual(response.data['title'], updated_data['title'])
        # Assert the book in the database is updated
        self.book1.refresh_from_db() # assuming a refresh method exists
        self.assertEqual(self.book1.title, updated_data['title'])

    def test_book_update_by_non_owner(self):
        """
        Ensure a different user cannot update another user's book.
        """
        self.client.force_login(self.user2)
        updated_data = {
            'title': 'The Catcher in the Rye (Attempted Update)',
            'author': 'J.D. Salinger',
            'publication_year': 1951
        }
        response = self.client.put(self.detail_url(self.book1.pk), updated_data, format='json')

        # Assert a 403 Forbidden status code
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Assert the book in the database remains unchanged
        self.book1.refresh_from_db() # assuming a refresh method exists
        self.assertNotEqual(self.book1.title, updated_data['title'])

    def test_book_delete_by_owner(self):
        """
        Ensure the book's owner can delete the book.
        """
        self.client.force_login(self.user1)
        response = self.client.delete(self.detail_url(self.book1.pk))

        # Assert a 204 No Content status code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Assert the book is no longer in the database
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_book_delete_by_non_owner(self):
        """
        Ensure a different user cannot delete another user's book.
        """
        self.client.force_login(self.user2)
        response = self.client.delete(self.detail_url(self.book1.pk))

        # Assert a 403 Forbidden status code
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Assert the book still exists in the database
        self.assertTrue(Book.objects.filter(pk=self.book1.pk).exists())
    
    def test_book_list_filtering(self):
        """
        Ensure books can be filtered by publication year.
        """
        response = self.client.get(self.list_url, {'publication_year': 1951})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # There should be two books published in 1951 if we were to have a model
        # For this mock, let's just check for the one we have
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Catcher in the Rye')
    
    def test_book_list_ordering(self):
        """
        Ensure books can be ordered by title in descending order.
        """
        response = self.client.get(self.list_url, {'ordering': '-title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'To Kill a Mockingbird')
        self.assertEqual(response.data[1]['title'], 'The Catcher in the Rye')
        self.assertEqual(response.data[2]['title'], '1984')
