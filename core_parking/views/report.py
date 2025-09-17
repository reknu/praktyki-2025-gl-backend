from rest_framework import generics
from ..models.report import Report
from ..serializers.report import ReportSerializer

class ReportCreateAPIView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer