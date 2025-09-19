# from rest_framework import viewsets
# from rest_framework.permissions import AllowAny
# from ..models import User
# from ..serializers import UserSerializer
# from rest_framework.permissions import IsAuthenticated
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [AllowAny]
#     permission_classes = [IsAuthenticated]