from django.urls import path , include
from .views import EmployeeList, UserList, ParkingList, ReservationList
from rest_framework.routers import DefaultRouter
from .views.vehicle import VehicleViewSet
router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
urlpatterns = [
    path('employees/', EmployeeList.as_view()),
    path('users/', UserList.as_view()),
    path('', include(router.urls)),
    path('parking/', ParkingList.as_view()),
    path('reservations/', ReservationList.as_view()),
]
