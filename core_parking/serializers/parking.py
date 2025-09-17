

from rest_framework import serializers
from ..models.parking import Parking

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
     
        fields = ['id', 'spot_number', 'floor', 'status']