from django.urls import path
from .views import EmployeeList, UserList, VehicleList, ParkingList, ReservationList

urlpatterns = [
    path('employees/', EmployeeList.as_view()),
    path('users/', UserList.as_view()),
    path('vehicles/', VehicleList.as_view()),
    path('parking/', ParkingList.as_view()),
    path('reservations/', ReservationList.as_view()),
]