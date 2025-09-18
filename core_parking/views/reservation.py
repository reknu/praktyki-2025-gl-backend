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
    
class UpdateReservation(generics.RetrieveUpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)
    
class GetReservationById(APIView):
    permission_classes = [IsAuthenticated]

def get(self, request, pk, *args, **kwargs):
    try:
        reservation = Reservation.objects.get(pk=pk, user=request.user)
    except Reservation.DoesNotExist:
        return Response(
            {"detail": "Reservation not found or you do not have permission."},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = ReservationSerializer(reservation)
    return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteReservationById(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        try:
            reservation = Reservation.objects.get(pk=pk, user=request.user)
        except Reservation.DoesNotExist:
            return Response(
                {"detail": "Reservation not found or you do not have permission."},
                status=status.HTTP_404_NOT_FOUND
            )
        reservation.delete()
        return Response({"detail": "Reservation deleted successfully."}, status=status.HTTP_200_OK)