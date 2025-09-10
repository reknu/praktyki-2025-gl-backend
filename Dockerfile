# Etap 0: Testy
FROM python:3.10-slim AS tester

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py test

# --- Builder Stage ---
FROM python:3.10-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gettext \
    && rm -rf /var/lib/apt/lists/*

COPY docker_settings.py .
ENV DJANGO_SETTINGS_MODULE=docker_settings

RUN python manage.py collectstatic --noinput

# --- Final Production Stage ---
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app /app
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# CHANGE: Use the correct project name
ENV DJANGO_SETTINGS_MODULE=parking_project.settings

EXPOSE 8000

# CHANGE: Use the correct project name
CMD ["/usr/local/bin/gunicorn", "--bind", "0.0.0.0:8000", "parking_project.wsgi:application"]