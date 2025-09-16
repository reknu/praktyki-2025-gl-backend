# W pliku core_parking/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.employee import EmployeeList
# Importuj widoki z ich plików, jak wcześniej
from .views.user import UserViewSet
from .views.vehicle import VehicleViewSet
from .views.parking import ParkingList
from .views.reservation import ReservationList
from .views.parking_detail import ParkingDetailWithAvailability
from .views.report import ReportCreateAPIView

# Poprawnie skonfigurowane routery
router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # Pozostaw tylko te ścieżki, które nie są obsługiwane przez router
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('parking/', ParkingList.as_view(), name='parking-list'),
    path('parking/<int:pk>/', ParkingDetailWithAvailability.as_view(), name='parking-detail'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
    path('report/', ReportCreateAPIView.as_view(), name='report-problem'),
    
    # Dołącz ścieżki z routera na końcu
    path('', include(router.urls)),
]