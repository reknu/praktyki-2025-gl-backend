# Uses a slim Python image to keep the final container size small.
FROM python:3.10-slim AS builder

# Set environment variables for Python
# PYTHONDONTWRITEBYTECODE=1 prevents Python from writing .pyc files
# PYTHONUNBUFFERED=1 forces stdout and stderr to be unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory for the application inside the container
WORKDIR /app

# Install build dependencies required for many Python packages,
# as well as `gettext` for static file internationalization.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gettext \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the core project files and applications
# Using the general COPY . . command as it is more robust,
# assuming manage.py and the project folder are in the root of the build context.
COPY . .

# Use the custom settings file for the build step
# This resolves the `ImproperlyConfigured` error by providing STATIC_ROOT
COPY docker_settings.py .
ENV DJANGO_SETTINGS_MODULE=docker_settings

# Run `collectstatic` to gather all static files
# The --noinput flag prevents interactive prompts during the build.
RUN python manage.py collectstatic --noinput

# A new, clean image to be used for production runtime.
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the installed site packages and the collected static files
# from the builder stage, keeping the final image lean.
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app /app

# The final image should use the standard settings file for the application to run
ENV DJANGO_SETTINGS_MODULE=praktyki-2025-gl-backend.settings

# Expose the port your Django application will be running on
EXPOSE 8000

# The command to start the application using Gunicorn
CMD ["/usr/local/bin/gunicorn", "--bind", "0.0.0.0:8000", "praktyki-2025-gl-backend.wsgi:application"]


