from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated

from users.models import User

from .serializers import CustomUserSerializer


class CustomUserViewSet(UserViewSet):
    """Получаем/создаем пользователей."""
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'post', 'delete')
    queryset = User.objects.all()
