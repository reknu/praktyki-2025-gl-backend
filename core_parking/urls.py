from django.urls import path
from .views.employee import EmployeeList
from .views.user import UserList
from .views.vehicle import VehicleList
from .views.parking import ParkingList
from .views.reservation import ReservationList
from .views.parking_detail import ParkingDetailWithAvailability

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('users/', UserList.as_view(), name='user-list'),
    path('vehicles/', VehicleList.as_view(), name='vehicle-list'),
    
    path('parking/', ParkingList.as_view(), name='parking-list'),  # To jest kluczowe, aby miało nazwę
    path('parking/<int:pk>/', ParkingDetailWithAvailability.as_view(), name='parking-detail'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
]


"""
from django.urls import path
from .views import EmployeeList, UserList, VehicleList, ParkingList, ReservationList
from .views.parking_detail import ParkingDetailWithAvailability
from core_parking import views
from .views.parking import ParkingList

urlpatterns = [
    path('employees/', EmployeeList.as_view()),
    path('users/', UserList.as_view()),
    path('vehicles/', VehicleList.as_view()),
    path('parking/', ParkingList.as_view()),
    path('parking/<int:pk>/', ParkingDetailWithAvailability.as_view(), name='parking-detail'),
    path('reservations/', ReservationList.as_view()),
    path('parking/<int:spot_id>/', ParkingDetailWithAvailability.as_view()),
]

"""