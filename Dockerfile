FROM python:3.11-slim AS builder

# Set the working directory for the application
WORKDIR /app

# Install system dependencies needed for some Python packages (e.g., psycopg2)
# 'apt-get update' and 'apt-get install' are chained in a single RUN command
# to reduce the number of image layers.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    # Clean up APT cache to keep the image small
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies from requirements.txt
# The '--no-cache-dir' flag prevents pip from caching packages, saving space
RUN pip install --no-cache-dir -r requirements.txt

# STAGE 2: Create the final, lean production image
# Use a minimal Python image for the final runtime environment
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy only the installed dependencies from the 'builder' stage
# This dramatically reduces the final image size by leaving behind
# the build tools and intermediate files.
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app /app

# Expose the port that Gunicorn will run on
EXPOSE 8000

# Collect static files. This step is crucial for production.
RUN python manage.py collectstatic --noinput

# Define the command to run the application using Gunicorn
# 'CMD' runs a web server that will be accessible on the exposed port
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]