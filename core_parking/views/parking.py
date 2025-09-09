from rest_framework import generics
from ..models import Parking
from ..serializers import ParkingSerializer

class ParkingList(generics.ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer