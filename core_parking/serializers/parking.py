from rest_framework import serializers
from ..models.parking import Parking

class ParkingSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Parking
        fields = '__all__'