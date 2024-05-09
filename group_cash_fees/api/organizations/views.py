from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from organizations.models import Organization

from .serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    """Чтение списка/объекта организация."""
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
