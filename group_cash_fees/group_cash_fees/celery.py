import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "group_cash_fees.settings")

app = Celery("group_cash_fees")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
