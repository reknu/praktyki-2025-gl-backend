

from rest_framework import generics, permissions
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

from ..models.parking import Parking
from ..models.reservation import Reservation
from ..serializers.parking import ParkingSerializer
from ..serializers.reservation import ReservationSerializer

class OccupiedParkingSpotsView(generics.ListAPIView):
    """
    Zwraca listę miejsc parkingowych, które są aktualnie ZAJĘTE.
    """
    serializer_class = ParkingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        now = timezone.now()
        active_spots_ids = Reservation.objects.filter(
            start_date__lte=now,
            end_date__gte=now
        ).values_list('spot_id', flat=True)
        return Parking.objects.filter(id__in=active_spots_ids)


class MyActiveReservationListView(generics.ListAPIView):
    """
    Zwraca listę aktywnych rezerwacji dla aktualnie
    zalogowanego użytkownika.
    """
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Reservation.objects.filter(
            user=user,
            end_date__gte=timezone.now()
        ).select_related('spot')