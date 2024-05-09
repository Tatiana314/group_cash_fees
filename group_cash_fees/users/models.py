from django.contrib.auth.models import AbstractUser
from django.db import models

USER_DATA = '{username} - {email} - {first_name} {last_name}'
MAX_LENGTH_EMAIL = 254
MAX_LENGTH_NAME_USER = 150


class User(AbstractUser):
    """Модель Пользователя."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]
    email = models.EmailField(
        unique=True, max_length=MAX_LENGTH_EMAIL, blank=False, null=False
    )
    first_name = models.CharField(
        'Имя', blank=False, null=False, max_length=MAX_LENGTH_NAME_USER
    )
    last_name = models.CharField(
        'Фамилия', blank=False, null=False, max_length=MAX_LENGTH_NAME_USER
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return USER_DATA.format(
            username=self.username,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name
        )
