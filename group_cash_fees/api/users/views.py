from djoser.views import UserViewSet
from rest_framework.permissions import AllowAny

from users.models import User

from .serializers import CustomUserSerializer


class CustomUserViewSet(UserViewSet):
    """Получаем/создаем пользователей."""
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)
    http_method_names = ('get', 'post', 'delete')
    queryset = User.objects.all()
