FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=babytracker.settings

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
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

# Create logs directory
RUN mkdir -p /app/logs

# Expose port
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Start command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "babytracker.wsgi:application"]
