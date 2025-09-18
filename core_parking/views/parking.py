from rest_framework import generics
from ..models.parking import Parking
from ..models.reservation import Reservation
from ..serializers.parking import ParkingSerializer
from django.db.models import Q, Case, When, Value
from django.utils import timezone
from datetime import datetime

class ParkingList(generics.ListCreateAPIView):
    serializer_class = ParkingSerializer

    def get_queryset(self):
        queryset = Parking.objects.all()
        now = timezone.now()
        
        floor_param = self.request.query_params.get('floor')
        if floor_param:
            try:
                floor_int = int(floor_param)
                queryset = queryset.filter(floor=floor_int)
            except ValueError:
                pass  
        start_time_str = self.request.query_params.get('start_time')
        end_time_str = self.request.query_params.get('end_time')
        
        if start_time_str and end_time_str:
            try:
                start_time = datetime.fromisoformat(start_time_str.replace('Z', '+00:00'))
                end_time = datetime.fromisoformat(end_time_str.replace('Z', '+00:00'))
            except (ValueError, TypeError):
                start_time, end_time = now, now
        else:
            start_time, end_time = now, now
        
        occupied_spot_ids = Reservation.objects.filter(
            Q(start_date__lte=end_time) & Q(end_date__gte=start_time)
        ).values_list('spot_id', flat=True)
        
        queryset = queryset.annotate(
            is_occupied=Case(
                When(id__in=occupied_spot_ids, then=Value(True)),
                default=Value(False)
            )
        )
        
        status_filter = self.request.query_params.get('status')
        if status_filter:
            if status_filter.upper() == 'FREE':
                queryset = queryset.filter(is_occupied=False)
            elif status_filter.upper() == 'OCCUPIED':
                queryset = queryset.filter(is_occupied=True)
                
        return queryset
