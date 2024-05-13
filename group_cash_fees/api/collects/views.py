from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from collects.models import Collect
#from api.permissions import AuthorOrReadOnly

from .serializers import GetCollectSerializer, CreateCollectSerializer


class CollectViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """Создание/чтение - групповой денежный сбор."""
    queryset = Collect.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return GetCollectSerializer
        return CreateCollectSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
