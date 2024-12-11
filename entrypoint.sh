#!/bin/sh


python manage.py migrate
echo "migrations done"

python fill_db.py
echo "DB filled"

python manage.py runserver 0.0.0.0:8000
