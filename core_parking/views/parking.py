from rest_framework import generics
from ..models.parking import Parking
from ..models.reservation import Reservation
from ..serializers.parking import ParkingSerializer
from django.db.models import Q
from django.utils import timezone

class ParkingList(generics.ListCreateAPIView):
    serializer_class = ParkingSerializer

    def get_queryset(self):
        # Pobierz wszystkie miejsca parkingowe
        queryset = Parking.objects.all()

        # Pobierz aktualny czas
        now = timezone.now()

        # Znajdź wszystkie rezerwacje, które są aktywne w tym momencie
        active_reservations = Reservation.objects.filter(
            Q(start_date__lte=now) & Q(end_date__gte=now)
        ).values_list('spot', flat=True)

        occupied_spot_ids = list(active_reservations)

        # Dynamicznie zaktualizuj status każdego miejsca w zestawie zapytań
        for parking_spot in queryset:
            if parking_spot.id in occupied_spot_ids:
                parking_spot.status = 1  # Zajęte
            else:
                parking_spot.status = 0  # Wolne
        
        # Nowa logika: Filtrowanie po dynamicznie obliczonym statusie
        status_filter = self.request.query_params.get('status')
        if status_filter is not None:
            # Tworzymy nową listę obiektów, aby móc je przefiltrować
            filtered_list = [spot for spot in queryset if str(spot.status) == status_filter]
            return Parking.objects.filter(id__in=[spot.id for spot in filtered_list])

        return queryset