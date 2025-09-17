# W pliku core_parking/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views.delete_user import DeleteUserView
# from .views.user import UserList, UserViewSet
# from .views.vehicle import VehicleList, VehicleViewSet
from .views.employee import EmployeeList
from .views.login import LoginView
from .views.parking import ParkingList
from .views.register import RegisterView
from .views.reservation import ReservationList
from .views.parking_detail import ParkingDetailWithAvailability
from .views.update_user import UpdateUserView
from .views.verify_jwt import JWTAccess
# from .views.user import UserViewSet
from .views.vehicle import VehicleViewSet
from .views.reservation import ReservationList, UserReservationsList, LatestFiveReservations
from .views.report import ReportCreateAPIView
# from .views.user import UserList, UserViewSet
# from .views.vehicle import VehicleList, VehicleViewSet


# router = DefaultRouter()
# router.register(r'vehicles', VehicleViewSet, basename='vehicle')
# router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('parking/', ParkingList.as_view(), name='parking-list'),
    path("register/", RegisterView.as_view(), name="register"),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/access/', JWTAccess.as_view(), name='verify_jwt'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('report/', ReportCreateAPIView.as_view(), name='report-problem'),
    # path('users/', UserList.as_view(), name='user-list'),
    # path('vehicles/', VehicleList.as_view(), name='vehicle-list'),
    path('parking/', ParkingList.as_view(), name='parking-list'),
    path('parking/<int:pk>/', ParkingDetailWithAvailability.as_view(), name='parking-detail'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'), # co robi samo reservations, tworzy moze?
    path('reservations/list', UserReservationsList.as_view(), name='reservation-list'),
    path('reservations/list/latest', LatestFiveReservations.as_view(), name='reservation-list'),
    path("user/update/", UpdateUserView.as_view(), name="user-update"),
    path("user/delete/", DeleteUserView.as_view(), name="user-delete"),
    # path('', include(router.urls)),
]