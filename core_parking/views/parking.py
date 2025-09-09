from rest_framework import generics
from ..models.parking import Parking
from ..models.reservation import Reservation
from ..serializers.parking import ParkingSerializer
from django.db.models import Q, Case, When, Value
from django.utils import timezone

class ParkingList(generics.ListCreateAPIView):
    serializer_class = ParkingSerializer

    def get_queryset(self):
        queryset = Parking.objects.all()

        status_filter = self.request.query_params.get('status')
        now = timezone.now()

        # Znajdź ID wszystkich miejsc, które są obecnie zajęte
        occupied_spot_ids = Reservation.objects.filter(
            Q(start_date__lte=now) & Q(end_date__gte=now)
        ).values_list('spot', flat=True)

        # Dynamicznie dodaj pole 'is_occupied' do każdego miejsca
        queryset = queryset.annotate(
            is_occupied=Case(
                When(id__in=occupied_spot_ids, then=Value(True)),
                default=Value(False)
            )
        )

        # Filtruj na podstawie parametru 'status'
        if status_filter:
            if status_filter.upper() == 'FREE':
                queryset = queryset.filter(is_occupied=False)
            elif status_filter.upper() == 'OCCUPIED':
                queryset = queryset.filter(is_occupied=True)

        return queryset