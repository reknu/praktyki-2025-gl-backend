from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core_parking.models import Parking, Reservation, Employee, User
from django.utils import timezone
from datetime import timedelta

class ParkingListTestCase(APITestCase):

    def setUp(self):
        self.parking_spot = Parking.objects.create(spot_number='A01', floor=1)
        self.employee = Employee.objects.create(first_name="Test", last_name="Employee", email="test@example.com")
        self.user = User.objects.create(password='testpassword', employee=self.employee)
        self.now = timezone.now()

    def test_list_all_parking_spots(self):
        """Testuje, czy endpoint zwraca wszystkie miejsca parkingowe."""
        response = self.client.get(reverse('parking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['status'], 'FREE')

    def test_list_with_current_reservation(self):
        """Testuje, czy miejsce jest pokazywane jako ZAJĘTE, jeśli jest aktualnie zarezerwowane."""
        Reservation.objects.create(
            spot=self.parking_spot,
            user=self.user,
            start_date=self.now - timedelta(hours=1),
            end_date=self.now + timedelta(hours=1)
        )
        response = self.client.get(reverse('parking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['status'], 'OCCUPIED')

    def test_filter_by_date_range(self):
        """Testuje filtrowanie miejsc według określonego zakresu dat."""
        start_time = self.now + timedelta(days=1, hours=10)
        end_time = self.now + timedelta(days=1, hours=12)
        Reservation.objects.create(
            spot=self.parking_spot,
            user=self.user,
            start_date=start_time,
            end_date=end_time
        )
        query_params = {
            'start_time': (self.now + timedelta(days=1, hours=11)).isoformat(),
            'end_time': (self.now + timedelta(days=1, hours=13)).isoformat(),
        }
        response = self.client.get(reverse('parking-list'), query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['status'], 'OCCUPIED')

    def test_filter_by_status(self):
        """Testuje filtrowanie miejsc po statusie (WOLNE lub ZAJĘTE)."""
        Reservation.objects.create(
            spot=self.parking_spot,
            user=self.user,
            start_date=self.now - timedelta(hours=1),
            end_date=self.now + timedelta(hours=1)
        )
        free_spot = Parking.objects.create(spot_number='A02', floor=1)

        response = self.client.get(reverse('parking-list'), {'status': 'OCCUPIED'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['spot_number'], 'A01')

        response = self.client.get(reverse('parking-list'), {'status': 'FREE'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['spot_number'], 'A02')

class ParkingDetailTestCase(APITestCase):

    def setUp(self):
        self.parking_spot = Parking.objects.create(spot_number='B01', floor=1)
        self.employee = Employee.objects.create(first_name="Test", last_name="Employee", email="test2@example.com")
        self.user = User.objects.create(password='testpassword', employee=self.employee)
        self.now = timezone.now()

    def test_get_parking_spot_by_id(self):
        """Testuje, czy można pobrać pojedyncze miejsce parkingowe."""
        response = self.client.get(reverse('parking-detail', args=[self.parking_spot.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'FREE')
        self.assertEqual(response.data['spot_number'], 'B01')

    def test_get_occupied_spot_with_current_reservation(self):
        """Testuje, czy miejsce jest pokazywane jako ZAJĘTE, jeśli jest aktualnie zarezerwowane, bez podawania filtrów."""
        Reservation.objects.create(
            spot=self.parking_spot,
            user=self.user,
            start_date=self.now - timedelta(hours=1),
            end_date=self.now + timedelta(hours=1)
        )
        response = self.client.get(reverse('parking-detail', args=[self.parking_spot.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'OCCUPIED')

    def test_get_spot_with_future_reservation(self):
        """Testuje, czy miejsce z przyszłą rezerwacją jest nadal WOLNE dla bieżącego czasu."""
        Reservation.objects.create(
            spot=self.parking_spot,
            user=self.user,
            start_date=self.now + timedelta(days=1),
            end_date=self.now + timedelta(days=1, hours=2)
        )
        response = self.client.get(reverse('parking-detail', args=[self.parking_spot.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'FREE')

    def test_filter_spot_by_date_range(self):
        """Testuje, czy status miejsca jest poprawnie określany dla podanego zakresu dat."""
        Reservation.objects.create(
            spot=self.parking_spot,
            user=self.user,
            start_date=self.now + timedelta(days=1, hours=10),
            end_date=self.now + timedelta(days=1, hours=12)
        )
        query_params = {
            'start_time': (self.now + timedelta(days=1, hours=11)).isoformat(),
            'end_time': (self.now + timedelta(days=1, hours=13)).isoformat(),
        }
        response = self.client.get(reverse('parking-detail', args=[self.parking_spot.id]), query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'OCCUPIED')