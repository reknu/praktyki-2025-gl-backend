

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from .models.user import User
from .models.parking import Parking
from .models.reservation import Reservation


class MyActiveReservationsEndpointTest(APITestCase):
    def setUp(self):
        self.user_one = User.objects.create(password='pass1')
        self.user_two = User.objects.create(password='pass2')
        self.spot = Parking.objects.create(spot_number='B1', floor=2)
        self.url = reverse('my-active-reservations-list')

    def test_unauthenticated_user_is_denied(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_with_no_reservations_gets_empty_list(self):
        self.client.force_authenticate(user=self.user_one)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_user_sees_their_active_reservation(self):
        Reservation.objects.create(
            user=self.user_one,
            spot=self.spot,
            start_date=timezone.now() - timedelta(hours=1),
            end_date=timezone.now() + timedelta(hours=1)
        )
        
        self.client.force_authenticate(user=self.user_one)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['spot'], self.spot.id)

    def test_user_does_not_see_other_users_reservations(self):
        Reservation.objects.create(
            user=self.user_two, 
            spot=self.spot,
            start_date=timezone.now() - timedelta(hours=1),
            end_date=timezone.now() + timedelta(hours=1)
        )
        
        # Logujemy się jako user_one
        self.client.force_authenticate(user=self.user_one)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Oczekujemy pustej listy, bo user_one nie ma rezerwacji
        self.assertEqual(len(response.data), 0)