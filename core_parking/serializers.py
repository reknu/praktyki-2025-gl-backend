from rest_framework import serializers
from .models import Pracownik, User, Pojazd, Parking, Rezerwacja

class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PojazdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pojazd
        fields = '__all__'

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'

class RezerwacjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezerwacja
        fields = '__all__'