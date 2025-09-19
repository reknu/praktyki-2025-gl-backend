from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Employee
from ..serializers import EmployeeSerializer

class EmployeeList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer