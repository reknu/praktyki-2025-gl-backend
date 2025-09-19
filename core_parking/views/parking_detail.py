from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models.parking import Parking
from ..models.reservation import Reservation
from ..serializers.parking import ParkingSerializer
from django.db.models import Q, Case, When, Value, F
from django.utils import timezone
from datetime import datetime
from rest_framework.exceptions import NotFound

class ParkingDetailWithAvailability(generics.RetrieveAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    # This line is added to require authentication for all requests to this view
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        spot_id = self.kwargs.get('pk')  # Get spot id from URL
        try:
            # The previous version used 'spot_number', but your URL config expects 'pk' (id).
            # The code is now fixed to use 'id' as the filter.
            parking_spot_queryset = Parking.objects.filter(id=spot_id)
            if not parking_spot_queryset.exists():
                raise NotFound("Parking spot not found.")
        except Parking.DoesNotExist:
            raise NotFound("Parking spot not found.")
        
        now = timezone.now()
        start_time = now
        end_time = now

        # Parse optional start_time and end_time query params
        start_time_str = self.request.query_params.get('start_time')
        end_time_str = self.request.query_params.get('end_time')
        if start_time_str and end_time_str:
            try:
                # Replace 'Z' and make the datetime objects timezone-aware
                start_time = timezone.make_aware(datetime.fromisoformat(start_time_str.replace('Z', '+00:00')))
                end_time = timezone.make_aware(datetime.fromisoformat(end_time_str.replace('Z', '+00:00')))
            except (ValueError, TypeError):
                pass

        # Determine if spot is occupied during requested timeframe
        occupied_spot_ids = Reservation.objects.filter(
            Q(start_date__lte=end_time) & Q(end_date__gte=start_time)
        ).values_list('spot_id', flat=True)
        
        parking_spot = parking_spot_queryset.annotate(
            is_occupied=Case(
                When(id__in=occupied_spot_ids, then=Value(True)),
                default=Value(False)
            )
        ).first()

        # Get the closest future reservation after now
        next_reservation = (
            Reservation.objects
            .filter(spot_id=parking_spot.id, start_date__gte=now)
            .order_by('start_date')
            .select_related('user')  # Assuming Reservation has a FK to User
            .first()
        )

        if next_reservation:
            parking_spot.next_reservation = {
                "full_name": f"{next_reservation.user.first_name} {next_reservation.user.last_name}",
                "email": next_reservation.user.email,
                "phone": next_reservation.user.phone_number,
                "start_date": next_reservation.start_date,
                "end_date": next_reservation.end_date,
            }
        else:
            parking_spot.next_reservation = None

        return parking_spot
