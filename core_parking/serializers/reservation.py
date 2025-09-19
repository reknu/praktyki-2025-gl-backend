from rest_framework import serializers
from ..models import Reservation
from .user import UserDetailSerializer
from .vehicle import VehicleSerializer
class ReservationSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)
    user = UserDetailSerializer(read_only=True)

    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=Reservation._meta.get_field("vehicle").remote_field.model.objects.all(),
        source="vehicle",
        write_only=True
    )

    class Meta:
        model = Reservation
        fields = [
            "id", "spot", "start_date", "end_date",
            "vehicle", "vehicle_id",  # both read + write
            "user"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is None:  # creation
            self.fields['start_date'].required = True
            self.fields['end_date'].required = True
        else:
            self.fields['start_date'].required = False
            self.fields['end_date'].required = False