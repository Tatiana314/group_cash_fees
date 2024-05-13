from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from collects.models import Collect

from .serializers import GetPaymentSerializer, CreatePaymentSerializer


class PaymentsViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    """Создание/чтение - платеж."""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return GetPaymentSerializer
        return CreatePaymentSerializer

    def collect_object(self):
        return get_object_or_404(Collect, id=self.kwargs.get("collect_id"))

    def get_queryset(self):
        return self.collect_object().payments.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, collect=self.collect_object())
