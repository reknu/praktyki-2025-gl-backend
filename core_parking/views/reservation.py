# core_parking/views/reservation.py

from rest_framework import generics
from ..models.reservation import Reservation
from ..serializers.reservation import ReservationSerializer

class ReservationList(generics.ListCreateAPIView):
    """
    Widok do listowania WSZYSTKICH rezerwacji 
    i tworzenia nowych. Endpoint jest teraz publiczny.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    # Usunęliśmy stąd linię 'permission_classes'
    # Usunęliśmy stąd metodę 'perform_create'