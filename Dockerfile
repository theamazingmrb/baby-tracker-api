FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=babytracker.settings

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    curl \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the Django project
COPY . .

# Install the package in development mode
RUN pip install -e .

# Set permissions
RUN chmod +x manage.py

# Expose port
EXPOSE 8000

# Create entrypoint script
RUN echo '#!/bin/bash\n\
cd /app/frontend && npm install && npm run build\n\
gunicorn --bind 0.0.0.0:8000 babytracker.wsgi:application' > /app/entrypoint.sh \
    && chmod +x /app/entrypoint.sh

# Start command
CMD ["/app/entrypoint.sh"]
