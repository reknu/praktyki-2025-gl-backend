from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Reservation, User
from ..serializers import ReservationSerializer
from rest_framework.views import APIView



class CreateReservation(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # user comes from token

class UserReservationsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user 
        reservations = Reservation.objects.filter(user=user).order_by("-start_date")
        serializer = ReservationSerializer(reservations, many=True)
        return Response({"detail":serializer.data}, status=status.HTTP_200_OK)


class LatestFiveReservations(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user  
        reservations = Reservation.objects.filter(user=user).order_by("-start_date")[:5]
        serializer = ReservationSerializer(reservations, many=True)
        return Response({"detail" :serializer.data} , status=status.HTTP_200_OK)