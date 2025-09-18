from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend 
from ..models import Reservation
from ..serializers.reservation import ReservationSerializer
from ..filters import ReservationFilter 

class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReservationFilter