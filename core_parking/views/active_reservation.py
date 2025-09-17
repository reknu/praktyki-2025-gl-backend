# core_parking/views/active_reservation.py

from rest_framework import generics, permissions
from django.utils import timezone

from ..models.parking import Parking
from ..models.reservation import Reservation
from ..serializers.parking import ParkingSerializer

# Dla czytelności, nazwijmy klasę tak, aby opisywała co robi
class OccupiedParkingSpotsView(generics.ListAPIView):
    """
    Zwraca listę miejsc parkingowych, które są aktualnie ZAJĘTE.
    """
    serializer_class = ParkingSerializer
    permission_classes = [permissions.AllowAny] # Endpoint będzie publiczny

    def get_queryset(self):
        now = timezone.now()

        # 1. Znajdź ID wszystkich miejsc, które mają aktywną (trwającą) rezerwację
        active_spots_ids = Reservation.objects.filter(
            start_date__lte=now,
            end_date__gte=now
        ).values_list('spot_id', flat=True)

        # 2. Zwróć tylko te miejsca parkingowe, których ID jest na powyższej liście
        return Parking.objects.filter(id__in=active_spots_ids)