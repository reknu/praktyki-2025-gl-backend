from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views.employee import EmployeeList
from .views.login import LoginView
# from .views.user import UserList, UserViewSet
# from .views.vehicle import VehicleList, VehicleViewSet
from .views.parking import ParkingList
from .views.register import RegisterView
from .views.reservation import ReservationList
from .views.parking_detail import ParkingDetailWithAvailability
from .views.verify_jwt import JWTAccess

router = DefaultRouter()
# router.register(r'vehicles', VehicleViewSet, basename='vehicle')
# router.register(r'users', UserViewSet, basename='user')
urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    # path('users/', UserList.as_view(), name='user-list'),
    # path('vehicles/', VehicleList.as_view(), name='vehicle-list'),
    path('parking/', ParkingList.as_view(), name='parking-list'),
    path("register/", RegisterView.as_view(), name="register"),
    path('parking/<int:pk>/', ParkingDetailWithAvailability.as_view(), name='parking-detail'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/access/', JWTAccess.as_view(), name='verify_jwt'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('', include(router.urls)),
]