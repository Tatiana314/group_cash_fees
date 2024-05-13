# group_cash_fees

Веб-сервис на базе Django, предоставляющий CRUD REST API для групповых денежных сборов.

## Технологии
Django, Django REST framework, Djoser, Drf-yasg, Celery, Redis


## Запуск проекта локально:
Клонировать репозиторий:
```
git clone https://github.com/Tatiana314/group_cash_fees.git && cd group_cash_fees
```
В директории group_cash_fees создать и активировать виртуальное окружение:
```
python -m venv venv
Linux/macOS: source env/bin/activate
windows: source env/scripts/activate
```
Проект использует базу данных PostgreSQL.
В директории group_cash_fees необходимо создать и заполнить ".env" с переменными окружения.
```
пример заполнения .env.example
```
Запустите docker compose:
```
docker compose up
```
Применение миграций и запуск приложение осуществляется автоматически.

Запустите celery:

```
docker compose exec backend bash
cd group_cash_fees
celery -A group_cash_fees worker -l info
```
Документация для API доступна по адресу http://127.0.0.1:8000/api/v1/redoc/. 
Документация представлена в формате Redoc.

Документация для API доступна по адресу http://127.0.0.1:8000/api/v1/swagger/. 
Документация представлена в формате Swagger.

### Команды управления Django
Реализована пользовательская команда управления Django:

python manage.py data_import_all - заполнение базы данных данными из файлов: users.csv, collects.csv, oganizations.csv, payments.csv, causes.csv. Данные файла необходимо расположить в директории static/data.


## Автор
[Мусатова Татьяна](https://github.com/Tatiana314)
