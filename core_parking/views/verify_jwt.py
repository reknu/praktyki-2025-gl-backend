from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models import User

class VerifyJWT(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(user_id=request.user.user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found", "code": "user_not_found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {"detail": "Token is valid."},
            status=status.HTTP_200_OK,
        )