from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Vehicle

class VehicleAPITests(APITestCase):

    def test_add_vehicle_success(self):
        valid_data = {
            "brand": "Toyota",
            "registration_number": "ZS 12345"
        }

        response = self.client.post('/api/vehicles/', valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vehicle.objects.count(), 1)
        self.assertEqual(Vehicle.objects.get().brand, "Toyota")

    def test_add_vehicle_missing_brand_fail(self):
        invalid_data = {
            "registration_number": "ZS 54321"
        }

        response = self.client.post('/api/vehicles/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Vehicle.objects.count(), 0)

    def test_add_vehicle_duplicate_registration_fail(self):
        Vehicle.objects.create(
            brand="Toyota",
            registration_number="ZS 55555"
        )
        duplicate_data = {
            "brand": "Nissan",
            "registration_number": "ZS 55555"
        }

        response = self.client.post('/api/vehicles/', duplicate_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(Vehicle.objects.count(), 1)