from rest_framework import viewsets
from ..serializers.vehicle import VehicleSerializer
from ..filters import VehicleFilter
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Vehicle

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = VehicleFilter