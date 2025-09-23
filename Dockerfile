# --- Final, Self-Contained Dockerfile ---
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies and certificate first
COPY github.crt /usr/local/share/ca-certificates/github.crt
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libpq-dev gettext && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install all Python packages directly to bypass build context issues
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir \
    asgiref==3.9.1 \
    Django==5.2.5 \
    djangorestframework==3.16.1 \
    djangorestframework-simplejwt \
    drf-spectacular \
    gunicorn==21.2.0 \
    sqlparse==0.5.3 \
    tzdata==2025.2

# Copy the entire application source code
COPY . .

# Copy the entrypoint script and make it executable
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose the port
EXPOSE 8000

# Set the entrypoint script as the startup command
ENTRYPOINT ["/app/entrypoint.sh"]