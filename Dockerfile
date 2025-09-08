# Use a lightweight Python base image
# We use a multi-stage build to keep the final image small and secure.

# Stage 1: Build dependencies and static files
FROM python:3.10-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies needed for some Python packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gettext \
    && rm -rf /var/lib/apt/lists/*

# Install project dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire project into the builder stage
COPY . .

# Run collectstatic to gather all static files
# The --noinput flag prevents interactive prompts during the build.
RUN python manage.py collectstatic --noinput

# Stage 2: Final production image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Temporarily set the settings module for the collectstatic command
ENV DJANGO_SETTINGS_MODULE=praktyki-2025-gl-backend.docker_settings

# Run collectstatic to gather all static files
RUN python manage.py collectstatic --noinput

# Reset the settings module if you need to, or set the final one for the app
ENV DJANGO_SETTINGS_MODULE=praktyki-2025-gl-backend.settings

# Copy only the necessary files from the builder stage
# This includes the installed dependencies and collected static files.
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app /app

# Expose the application port
EXPOSE 8000

# Run the Django application with Gunicorn for production
# This command should be specified in your docker-compose.yml
# For local development, you might use `python manage.py runserver` instead.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "praktyki-2025-gl-backend.wsgi:application"]
