from django.db import models
from django.forms import ValidationError

from organizations.models import Organization
from users.models import User


class Cause(models.Model):
    """Повод сбора денежных средств."""

    name = models.CharField("Название", max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Повод'
        verbose_name_plural = 'Поводы'


class Collect(models.Model):
    """Групповой денежный сбор."""

    name = models.CharField("Название", unique=True, max_length=50)
    description = models.TextField("Описание")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="collects",
        verbose_name="Автор",
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="collects",
        verbose_name="Организация",
    )
    cause = models.CharField("Повод", max_length=40)
    create_date = models.DateTimeField("Дата создания", auto_now_add=True)
    close_date = models.DateTimeField(
        "Дата завершения", blank=True, default=None
    )
    max_amount = models.PositiveIntegerField(
        "Максимальная сумма", blank=True, default=0
    )
    image = models.ImageField('Изображение', upload_to='collects/images/')

    def clean(self):
        if self.close_date and self.close_date <= self.create_date:
            raise ValidationError(
                'Дата завершения сбора не может быть меньше даты создания.'
            )

    def __str__(self) -> str:
        return f'{self.name}, {self.author}'

    class Meta:
        verbose_name = 'Денежный сбор'
        verbose_name_plural = 'Денежные сборы'
