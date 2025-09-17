
from rest_framework import serializers
from ..models.reservation import Reservation
from ..models.user import User

class ReservationSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Reservation
     
        fields = ['id', 'spot', 'start_date', 'end_date', 'user']