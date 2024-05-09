import logging
import os
import psycopg2

import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand

logging.basicConfig(
    level=logging.INFO, format=('%(asctime)s - %(levelname)s - %(message)s')
)

SERIES_NAME = {'category': 'category_id', 'author': 'author_id'}
PATH_TABLE = (
    ('static/data/users.csv', 'users_user'),
    ('static/data/collects.csv', 'collects_collect'),
    ('static/data/organizations.csv', 'organizations_organization'),
    ('static/data/payments.csv', 'payments_payment'),
    ('static/data/causes.csv', 'collects_cause'),
)
MESSAGE = 'Импорт из файла {path} в таблицу {table} осуществлен.'


class Command(BaseCommand):
    """Импорт группы файлов в БД."""

    help = 'Импорт данных из файлов в БД'

    def handle(self, *args, **kwargs):
        connection = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        for path, table in PATH_TABLE:
            try:
                data = pd.read_csv(
                    os.path.join(settings.BASE_DIR, path), index_col=0
                )
                data.rename(columns=SERIES_NAME).to_sql(
                    table, connection, if_exists="append", index=False
                )
                logging.info(MESSAGE.format(table=table, path=path))
            except Exception as error:
                logging.error(error)
