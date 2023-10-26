#!/bin/bash
# enter the folder
cd /exchange/exchange

ectstatic --noinput

echo "Make database makemigrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
