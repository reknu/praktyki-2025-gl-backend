# W pliku core_parking/serializers/report.py

from rest_framework import serializers
from ..models.report import Report
from ..models.employee import Employee
from ..models.parking import Parking # Upewnij się, że masz ten import

class ReportSerializer(serializers.ModelSerializer):
    reporter_name = serializers.SerializerMethodField(read_only=True)
    parking_spot_number = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Report
        fields = ['id', 'reporter', 'reporter_name', 'parking_spot', 'parking_spot_number', 'description', 'reported_at']
        read_only_fields = ['reported_at', 'reporter_name', 'parking_spot_number']
        extra_kwargs = {
            'reporter': {'write_only': True},
            'parking_spot': {'write_only': True},
        }

    def get_reporter_name(self, obj):
        return f"{obj.reporter.first_name} {obj.reporter.last_name}"

    def get_parking_spot_number(self, obj):
        return obj.parking_spot.spot_number