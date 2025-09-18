from rest_framework import serializers
from ..models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is None:  # creation
            self.fields['start_date'].required = True
            self.fields['end_date'].required = True
        else:
            self.fields['start_date'].required = False
            self.fields['end_date'].required = False
