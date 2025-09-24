from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

# --- Poprawione importy ---
from .views.vehicle import VehicleViewSet # ZMIANA: Importujemy ViewSet zamiast pojedynczych widoków
from .views.user import UserViewSet
# ... reszta Twoich importów bez zmian
from .views.delete_user import DeleteUserView
from .views.employee import EmployeeList
from .views.admin import AdminList
from .views.login import LoginView, LoginByToken
from .views.parking import ParkingList
from .views.register import RegisterView
from .views.parking_detail import ParkingDetailWithAvailability
from .views.update_user import UpdateUserView
from .views.verify_jwt import JWTAccess
from .views.reservation import CreateReservation, UserReservationsList, LatestFiveReservations, UpdateReservation, DeleteReservationById, GetReservationById
from .views.report import ReportCreateAPIView

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),

    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('admin/', AdminList.as_view(), name='admin'),
    path('parking/', ParkingList.as_view(), name='parking-list'),
    path('parking/<int:pk>/', ParkingDetailWithAvailability.as_view(), name='parking-detail'),
    path("register/", RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('token/login/', LoginByToken.as_view(), name='login-by-token'),
    path('token/access/', JWTAccess.as_view(), name='verify_jwt'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('report/', ReportCreateAPIView.as_view(), name='report-problem'),
    path("user/update/", UpdateUserView.as_view(), name="user-update"),
    path("user/delete/", DeleteUserView.as_view(), name="user-delete"),
    path('reservations/create/', CreateReservation.as_view(), name='reservation-create'),
    path('reservations/list/', UserReservationsList.as_view(), name='reservation-list'),
    path('reservations/list/latest/', LatestFiveReservations.as_view(), name='latest-reservations'),
    path("reservations/<int:pk>/", GetReservationById.as_view(), name="get-reservation"),
    path('reservations/<int:pk>/update/', UpdateReservation.as_view(), name='reservation-update'),
    path('reservations/<int:pk>/delete/', DeleteReservationById.as_view(), name='reservation-delete'),
]