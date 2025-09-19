

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.employee import EmployeeList
from .views.admin import AdminList
from .views.parking import ParkingList
from .views.reservation import ReservationList
from .views.vehicle import VehicleViewSet
from .views.user import UserViewSet
from .views.parking_detail import ParkingDetailWithAvailability
router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'users', UserViewSet, basename='user')
urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('parking/', ParkingList.as_view(), name='parking-list'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
    path('parking/<int:pk>/', ParkingDetailWithAvailability.as_view(), name='parking-detail'),
    path('admin/', AdminList.as_view(), name='admin'),
    path('', include(router.urls)),
]