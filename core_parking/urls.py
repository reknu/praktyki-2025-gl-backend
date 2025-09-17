# W pliku core_parking/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.employee import EmployeeList
# from .views.user import UserList, UserViewSet
# from .views.vehicle import VehicleList, VehicleViewSet
from .views.user import UserViewSet
from .views.vehicle import VehicleViewSet
from .views.parking import ParkingList
from .views.reservation import ReservationList, UserReservationsList, LatestFiveReservations
from .views.parking_detail import ParkingDetailWithAvailability
from .views.report import ReportCreateAPIView

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('parking/', ParkingList.as_view(), name='parking-list'),
    path('parking/<int:pk>/', ParkingDetailWithAvailability.as_view(), name='parking-detail'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
    path('report/', ReportCreateAPIView.as_view(), name='report-problem'),
    path('users/', UserList.as_view(), name='user-list'),
    path('vehicles/', VehicleList.as_view(), name='vehicle-list'),
    path('parking/', ParkingList.as_view(), name='parking-list'),
    path('parking/<int:pk>/', ParkingDetailWithAvailability.as_view(), name='parking-detail'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'), # co robi samo reservations, tworzy moze?
    path('reservations/list', UserReservationsList.as_view(), name='reservation-list'),
    path('reservations/list', LatestFiveReservations.as_view(), name='reservation-list'),
    path('', include(router.urls)),
]