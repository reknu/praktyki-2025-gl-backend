import uuid

from rest_framework import serializers
from ..models import User
import re    # Importujemy moduł do obsługi wyrażeń regularnych

def validate_password( value):
    if len(value) < 8:
        raise serializers.ValidationError("Password shall be at least 8 characters.")
    if not re.search(r'[A-Z]', value):
        raise serializers.ValidationError("Password shall contain at least one capital letter.")
    if not re.search(r'[!@#$%^&*()_+-=\[\]{};\':"\\|,.<>\/?~`]', value):
        raise serializers.ValidationError("Password shall contain at least one special character.")
    return value

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})


    def validate_password(self, value):
        return validate_password(value)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "full_name", "phone_number", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        return validate_password(value)

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            full_name=validated_data["full_name"],
            phone_number=validated_data["phone_number"],
            user_id=str(uuid.uuid4()),  # ensure a unique ID
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

