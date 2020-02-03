# Real-time Forex API
Real-time stock market API built with Beautiful Soup & Django REST Framework

## Getting Started

This tutorial works on **Python 3+** and Django 2+.

Install dependencies:

```
python3 -m pip3 install -r requirements.txt
```

run following commands:

```
python manage.py makemigrations forexAPI
python manage.py migrate
python manage.py runserver
```
and start Celery worker:

```
celery -A trading worker -l info
```

## Disclamier
This project created only for educational purposes. Do not use the project in production without owner permission otherwise I am not responsible for any action.

