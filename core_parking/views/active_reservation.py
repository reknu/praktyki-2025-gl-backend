

from rest_framework import generics, permissions
from django.utils import timezone

from ..models.parking import Parking
from ..models.reservation import Reservation
from ..serializers.parking import ParkingSerializer


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