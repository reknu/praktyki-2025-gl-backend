from rest_framework import serializers
from ..models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    spot = serializers.PrimaryKeyRelatedField(queryset=Reservation._meta.get_field("spot").related_model.objects.all())
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Reservation._meta.get_field("vehicle").related_model.objects.all())

    class Meta:
        model = Reservation
        fields = ["id", "start_date", "end_date", "spot", "vehicle", "user"]
        extra_kwargs = {
            "user": {"read_only": True},  # user is always taken from token
        }