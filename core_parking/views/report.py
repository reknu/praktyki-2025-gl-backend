from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models.report import Report
from ..serializers.report import ReportSerializer

class ReportCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer