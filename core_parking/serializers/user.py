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


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "username", "full_name", "email", "phone_number", "is_active", "is_staff"]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("Użytkownik o tej nazwie już istnieje.")
        return value

    def validate_password(self, value):
        return validate_password(value)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "full_name", "phone_number", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        return validate_password(value)

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            full_name=validated_data["full_name"],
            phone_number=validated_data["phone_number"],
            email=validated_data["email"],
            user_id=str(uuid.uuid4()),  # ensure a unique ID
        )
        user.set_password(validated_data["password"])
        user.save()
        return user



class UpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=False, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ["username", "full_name", "phone_number", "email", "password"]
        extra_kwargs = {
            "username": {"required": False},
            "full_name": {"required": False},
            "phone_number": {"required": False},
            "email": {"required": False},
            "password": {"required": False},
        }

    def validate_password(self, value):
        if value:
            return validate_password(value)
        return value


    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance