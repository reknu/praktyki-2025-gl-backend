# core_parking/views.py
from rest_framework import generics
from .models import Pracownik, User, Pojazd, Parking, Rezerwacja
from .serializers import PracownikSerializer, UserSerializer, PojazdSerializer, ParkingSerializer, RezerwacjaSerializer

class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PojazdList(generics.ListCreateAPIView):
    queryset = Pojazd.objects.all()
    serializer_class = PojazdSerializer

class ParkingList(generics.ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

class RezerwacjaList(generics.ListCreateAPIView):
    queryset = Rezerwacja.objects.all()
    serializer_class = RezerwacjaSerializer