#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start server
echo "Starting server..."
gunicorn --bind 0.0.0.0:8000 parking_project.wsgi:application