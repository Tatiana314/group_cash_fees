# Generated by Django 5.0.6 on 2024-05-09 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collects', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Picture',
        ),
        migrations.AlterField(
            model_name='collect',
            name='max_amount',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Максимальная сумма'),
        ),
    ]
