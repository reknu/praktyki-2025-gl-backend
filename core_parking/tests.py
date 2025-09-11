from django.test import TestCase, Client
from django.urls import reverse

class CoreParkingURLTests(TestCase):
    """
    Test suite for checking the availability of core_parking URLs.
    """
    def setUp(self):
        """
        Set up a test client for all tests in this class.
        """
        self.client = Client()

    def test_users_list_url_is_accessible(self):
        """
        Tests if the '/users/' endpoint is accessible and returns a 200 OK status.
        This confirms the URL and view are connected correctly.
        """
        # 'reverse' is a robust way to get the URL for a given view name
        # Assuming you have a name in your urls.py like: path('users/', UserList.as_view(), name='user-list')
        # For now, we'll use the hardcoded path.
        url = '/users/'
        
        # The client makes a GET request to the URL
        response = self.client.get(url)
        
        # We assert that the HTTP status code is 200, which means "OK"
        self.assertEqual(response.status_code, 200)
