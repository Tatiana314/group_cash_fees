from djoser.conf import settings
from rest_framework import serializers

from users.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    """Модель пользователя."""

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD
        )
        read_only_fields = (settings.LOGIN_FIELD,)


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name")
