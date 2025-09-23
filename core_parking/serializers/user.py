from rest_framework import serializers
from ..models import User
import re    # Importujemy moduł do obsługi wyrażeń regularnych

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    password = serializers.CharField(
        write_only=True, 
        style={'input_type': 'password'}
    )

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("Użytkownik o tej nazwie już istnieje.")
        return value

    def validate_password(self, value):

        if len(value) < 8:
            raise serializers.ValidationError("Hasło musi mieć co najmniej 8 znaków.")
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Hasło musi zawierać co najmniej jedną wielką literę.")
        if not re.search(r'[!@#$%^&*()_+-=\[\]{};\':"\\|,.<>\/?~`]', value):
            raise serializers.ValidationError("Hasło musi zawierać co najmniej jeden znak specjalny.")
        return value

def create(self, validated_data):

    User.set_password(validated_data['password'])
    User.save()
    return validated_data