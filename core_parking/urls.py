from django.urls import path , include
from .views import EmployeeList, ParkingList, ReservationList
from rest_framework.routers import DefaultRouter
from .views.vehicle import VehicleViewSet
from .views.user import  UserViewSet
router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'users', UserViewSet, basename='user')
urlpatterns = [
    path('employees/', EmployeeList.as_view()),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('parking/', ParkingList.as_view()),
    path('reservations/', ReservationList.as_view()),
]
