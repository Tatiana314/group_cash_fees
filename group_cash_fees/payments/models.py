from django.core.validators import MinValueValidator
from django.db import models

from collects.models import Collect
from users.models import User

DATA = (
    '{user}, {comment:.15}, {type}, {collect}, '
    '{invest_amount}, {create_date:%Y-%m-%d}, {public}'
)


class Payment(models.Model):
    """Пожертвование."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="Плательщик",
    )
    type = models.BooleanField("Ежемесячное пожертвование", default=False)
    collect = models.ForeignKey(
        Collect,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="Денежный сбор",
    )
    invest_amount = models.PositiveIntegerField(
        "Сумма пожертвования", validators=[MinValueValidator(50),]
    )
    create_date = models.DateTimeField("Дата создания", auto_now_add=True)
    comment = models.TextField("Комментарий")
    public = models.BooleanField("Сумма публична", default=True)

    def __str__(self):
        return DATA.format(
            user=self.user,
            type=self.type,
            collect=self.collect.name,
            invest_amount=self.invest_amount,
            create_date=self.create_date,
            comment=self.comment,
            public=self.public
        )
