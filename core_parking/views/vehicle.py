from rest_framework import viewsets
from ..models import Vehicle
from ..serializers import VehicleSerializer
from rest_framework.permissions import AllowAny

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [AllowAny]