# core_parking/serializers/reservation.py
from rest_framework import serializers
from ..models.reservation import Reservation
from ..models.user import User

class ReservationSerializer(serializers.ModelSerializer):
    # Pole user pozostaje listą rozwijaną
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Reservation
        # Usunęliśmy stąd jawną definicję pola 'spot',
        # ponieważ teraz jest to zwykły CharField i serializer obsłuży go automatycznie.
        fields = ['id', 'spot', 'start_date', 'end_date', 'user']