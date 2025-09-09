from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.parking import Parking
from ..serializers.parking import ParkingSerializer
from ..models.reservation import Reservation
from django.db.models import Q
from django.utils import timezone
from datetime import datetime

class ParkingDetailWithAvailability(APIView):
    def get(self, request, spot_id, *args, **kwargs):
        try:
            parking_spot = Parking.objects.get(id=spot_id)
        except Parking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        start_time_str = request.query_params.get('start_time')
        end_time_str = request.query_params.get('end_time')

        if start_time_str and end_time_str:
            try:
                start_time = datetime.fromisoformat(start_time_str)
                end_time = datetime.fromisoformat(end_time_str)

                if timezone.is_naive(start_time):
                    start_time = timezone.make_aware(start_time)
                if timezone.is_naive(end_time):
                    end_time = timezone.make_aware(end_time)

                conflicting_reservations = Reservation.objects.filter(
                    Q(spot_id=parking_spot.id) &
                    Q(start_date__lte=end_time) &
                    Q(end_date__gte=start_time)
                ).exists()

                parking_spot.status = 'OCCUPIED' if conflicting_reservations else 'FREE'

            except (ValueError, TypeError):
                pass # Ignore if dates are invalid, return original status

        serializer = ParkingSerializer(parking_spot)
        return Response(serializer.data)