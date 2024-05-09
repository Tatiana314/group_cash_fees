from rest_framework import serializers

from organizations.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """Модель Organization."""
    class Meta:
        fields = '__all__'
        model = Organization


class GetOrganizationSerializer(serializers.ModelSerializer):
    """Модель Organization."""
    class Meta:
        fields = ("name",)
        model = Organization
