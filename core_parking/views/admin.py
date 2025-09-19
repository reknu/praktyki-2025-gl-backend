from rest_framework import generics
from ..models import Admin
from ..serializers import AdminSerializer
from rest_framework.permissions import AllowAny

class AdminList(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [AllowAny]