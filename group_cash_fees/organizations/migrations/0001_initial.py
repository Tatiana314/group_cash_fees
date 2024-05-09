# Generated by Django 5.0.6 on 2024-05-09 09:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(verbose_name='Описание')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=400, verbose_name='Адресс')),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Некорректный ввод номера.', regex='^8([0-9]{10})$')], verbose_name='Телефон')),
            ],
        ),
    ]
