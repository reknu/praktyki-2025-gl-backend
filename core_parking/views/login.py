from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError

from ..models import User
from ..serializers.user import LoginSerializer, UserDetailSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"detail": "Username and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Validate login input
        serializer = LoginSerializer(data={"username": username, "password": password})
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"detail": e.detail}, status=status.HTTP_400_BAD_REQUEST)

        # Check password
        if not check_password(password, user.password):
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Generate tokens
        tokens = get_tokens_for_user(user)

        # Serialize full user details
        user_data = UserDetailSerializer(user).data

        return Response(
            {
                "user": user_data,
                "refresh": tokens["refresh"],
                "access": tokens["access"],
            },
            status=status.HTTP_200_OK,
        )
