from django.urls import path
from .views import PracownikList, UserList, PojazdList, ParkingList, RezerwacjaList

urlpatterns = [
    path('pracownicy/', PracownikList.as_view()),
    path('users/', UserList.as_view()),
    path('pojazdy/', PojazdList.as_view()),
    path('parkingi/', ParkingList.as_view()),
    path('rezerwacje/', RezerwacjaList.as_view()),
]