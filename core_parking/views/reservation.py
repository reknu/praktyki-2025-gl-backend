

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

