from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Reservation, User
from ..serializers import ReservationSerializer
from rest_framework.views import APIView

class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class UserReservationsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        username = request.query_params.get("username")
        if not username:
            return Response(
                {"detail": "Username query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"detail": f"User with username '{username}' not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        reservations = Reservation.objects.filter(user=user).order_by("-start_date")
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LatestFiveReservations(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        username = request.query_params.get("username")
        if not username:
            return Response(
                {"detail": "Username query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"detail": f"User with username '{username}' not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        reservations = Reservation.objects.filter(user=user).order_by("-start_date")[:5]
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)