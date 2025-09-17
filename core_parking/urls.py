# core_parking/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importujemy wszystkie potrzebne widoki z ich własnych plików
from .views.employee import EmployeeList
from .views.vehicle import VehicleList
from .views.parking import ParkingList
from .views.user import UserViewSet
from .views.reservation import ReservationList 
from .views.active_reservation import OccupiedParkingSpotsView 

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('vehicles/', VehicleList.as_view(), name='vehicle-list'),
    path('parking/', ParkingList.as_view(), name='parking-list'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
    
    # Nowy, poprawny endpoint pokazujący ZAJĘTE miejsca
   path('parking/occupied/', OccupiedParkingSpotsView.as_view(), name='occupied-parking-list'),
    
    path('', include(router.urls)),
]