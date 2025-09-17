from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core_parking.serializers.user import RegisterSerializer

class RegisterView(APIView):
    REQUIRED_FIELDS = ["username", "full_name", "phone_number", "password"]

    def post(self, request, *args, **kwargs):
        missing_fields = [f for f in self.REQUIRED_FIELDS if not request.data.get(f)]
        if missing_fields:
            return Response(
                {"detail": f"{', '.join(missing_fields)} are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "detail": "User registered successfully.",
                },
                status=status.HTTP_201_CREATED,
            )

        # This catches other validation errors like password complexity
        return Response(
            {"detail": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
