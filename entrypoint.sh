#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input

daphne core.asgi:application -b 0.0.0.0 -p 8000