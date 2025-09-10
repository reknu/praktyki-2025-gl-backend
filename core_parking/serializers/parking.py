# W pliku serializers.py
from rest_framework import serializers
from ..models.parking import Parking

class ParkingSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Parking
        fields = ('id', 'spot_number', 'floor', 'status')

    def get_status(self, obj):
        # Sprawdź, czy obiekt ma atrybut 'is_occupied',
        # który dodajemy w widoku (get_queryset).
        if hasattr(obj, 'is_occupied'):
            return 'OCCUPIED' if obj.is_occupied else 'FREE'
        return 'FREE' # Domyślny status, jeśli is_occupied nie istnieje.