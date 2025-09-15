
from django.urls import path
from .views.employee import EmployeeList
from .views.user import UserList
from .views.vehicle import VehicleList
from .views.parking import ParkingList
from .views.reservation import ReservationList
from .views.parking_detail import ParkingDetailWithAvailability
from rest_framework.routers import DefaultRouter
from .views.vehicle import VehicleViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('users/', UserList.as_view(), name='user-list'),
    path('vehicles/', VehicleList.as_view(), name='vehicle-list'),
    path('', include(router.urls)),
    path('parking/', ParkingList.as_view(), name='parking-list'),  # To jest kluczowe, aby miało nazwę
    path('parking/<int:pk>/', ParkingDetailWithAvailability.as_view(), name='parking-detail'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
]


