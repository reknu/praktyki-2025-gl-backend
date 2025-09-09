from django.urls import path, include
from .views import EmployeeList, VehicleList, ParkingList, ReservationList
from rest_framework.routers import DefaultRouter
from .views.user import UserViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = [
    path('employees/', EmployeeList.as_view()),
    path('', include(router.urls)),
    path('vehicles/', VehicleList.as_view()),
    path('parking/', ParkingList.as_view()),
    path('reservations/', ReservationList.as_view()),
]
