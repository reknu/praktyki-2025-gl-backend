from rest_framework import generics
from ..models.parking import Parking
from ..models.reservation import Reservation
from ..serializers.parking import ParkingSerializer
from django.db.models import Q, Case, When, Value
from django.utils import timezone
from datetime import datetime
from rest_framework.exceptions import NotFound

class ParkingDetailWithAvailability(generics.RetrieveAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    
    def get_object(self):
        spot_id = self.kwargs.get('pk') # Pobiera 'spot_id' z URL-a, ale klasa View używa 'pk'
        try:
            parking_spot_queryset = Parking.objects.filter(id=spot_id)
            if not parking_spot_queryset.exists():
                raise NotFound("Parking spot not found.")
        except Parking.DoesNotExist:
            raise NotFound("Parking spot not found.")
            
        now = timezone.now()
        start_time = now
        end_time = now
        
        start_time_str = self.request.query_params.get('start_time')
        end_time_str = self.request.query_params.get('end_time')

        if start_time_str and end_time_str:
            try:
                start_time = datetime.fromisoformat(start_time_str.replace('Z', '+00:00'))
                end_time = datetime.fromisoformat(end_time_str.replace('Z', '+00:00'))
            except (ValueError, TypeError):
                pass
        
        occupied_spot_ids = Reservation.objects.filter(
            Q(start_date__lte=end_time) & Q(end_date__gte=start_time)
        ).values_list('spot_id', flat=True)
        
        # Użyj annotate, tak jak w widoku listy, aby dynamicznie dodać pole
        parking_spot = parking_spot_queryset.annotate(
            is_occupied=Case(
                When(id__in=occupied_spot_ids, then=Value(True)),
                default=Value(False)
            )
        ).first()

        return parking_spot