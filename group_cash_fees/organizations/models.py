from django.db import models
from django.core.validators import RegexValidator

DATA = (
    '{name}, {description:.15}, {email}, {address}, {invest_amount}'
)
MAX_LENGTH_EMAIL = 254
MAX_LENGTH_ADRESS = 400
MAX_LENGTH_PHONE = 11


class Organization(models.Model):
    """Некоммерческая организация."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField("Описание")
    email = models.EmailField(
        unique=True, max_length=MAX_LENGTH_EMAIL, blank=False, null=False
    )
    address = models.CharField("Адресс", max_length=MAX_LENGTH_ADRESS)
    phone_number = models.CharField(
        'Телефон',
        max_length=MAX_LENGTH_PHONE,
        validators=[RegexValidator(
            regex='^8([0-9]{10})$', message='Некорректный ввод номера.'
        ),])
    
    def __str__(self):
        return DATA.format(
            name=self.name,
            description=self.description,
            email=self.email,
            address=self.address,
            cphone_number=self.phone_number,
        )
