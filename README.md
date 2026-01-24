# Baby Tracker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-4.2.10-green.svg)](https://www.djangoproject.com/)
[![UV](https://img.shields.io/badge/UV-lightning__fast__package__manager-purple.svg)](https://github.com/astral-sh/uv)

**Baby Tracker** is a complete solution for tracking your baby's daily activities including feedings, diaper changes, sleep patterns, growth milestones, and more. Built with privacy and security in mind, giving you full control over your baby's data.

---

## Overview

Baby Tracker helps you stay organized and informed about your baby's daily routine. From feeding schedules to sleep patterns, growth milestones to doctor appointments - everything you need in one secure, private place. Perfect for busy parents who want to track their baby's development without worrying about data privacy.

## Features

### Daily Tracking
- **🍼 Feedings**: Breastfeeding, bottle feeding, and solid foods with detailed tracking including side and quantity
- **👕 Diaper Changes**: Keep track of wet, dirty, and mixed diapers with timestamps
- **😴 Sleep Sessions**: Monitor nap times and nighttime sleep patterns with start/end times
- **📏 Growth Milestones**: Height, weight, and important developmental milestones with notes
- **🏥 Doctor Appointments**: Never miss a checkup or vaccination with doctor details and location
- **💊 Medications**: Track doses, frequency, and timing for any medications with start/end dates
- **🤱 Pumping Sessions**: For breastfeeding moms tracking milk supply with side and quantity
- **⏰ Reminders**: Set helpful reminders for feeding times, appointments, and more
- **🎯 Developmental Milestones**: Track physical, social, cognitive, language, and emotional milestones
- **📖 Recipe Management**: Store and organize baby food recipes with ingredients and instructions

### Smart Features
- **🤖 AI Insights**: Get personalized recommendations based on your baby's patterns
- **📱 Recipe Management**: Store and organize baby food recipes
- **⏰ Reminders**: Set helpful reminders for feeding times, appointments, and more
- **🔒 Secure Access**: Your data stays private and secure

## Architecture

### Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| **Backend Framework** | Django | 4.2.10 |
| **API Framework** | Django REST Framework | 3.14.0 |
| **Database** | PostgreSQL | Latest |
| **Package Manager** | UV | Latest |
| **Authentication** | JWT (djangorestframework-simplejwt) | 5.2.2 |
| **Documentation** | OpenAPI 3.0 (drf-spectacular) | 0.26.5 |
| **Data Analysis** | Pandas, NumPy, SciPy, Scikit-learn | Latest |
| **Caching** | Redis | Latest |
| **Rate Limiting** | django-ratelimit | 4.1.0 |

### Security Features

- **🔒 Security Hardening**: XSS protection, secure headers, HTTPS enforcement
- **⚡ Rate Limiting**: User-based rate limiting (100-1000 requests/hour)
- **🗄️ Database Optimization**: Strategic indexing for lightning-fast queries
- **📊 Structured Logging**: Comprehensive logging with file and console output
- **💾 Redis Caching**: High-performance caching layer
- **🛡️ Permission System**: Robust user/baby ownership validation
- **📈 Monitoring Ready**: Debug toolbar and observability features

## Installation

### Prerequisites

Before you begin, make sure you have these installed:

**For Docker Setup (Recommended):**
```bash
# Check Docker is installed
docker --version

# Check Docker Compose is available
docker-compose --version
```

**For Manual Setup:**
```bash
# Check Python version (needs 3.11)
python --version

# Check if PostgreSQL is available
psql --version

# Check if Redis is available
redis-cli --version

# Check if UV is installed
uv --version
```

### Installation Options

You have two ways to set up the Baby Tracker API:

#### Option 1: Docker Setup (Recommended)

**Quick Start with Docker Compose**

```bash
# Clone the repository
git clone https://github.com/theamazingmrb/baby-tracker-api.git
cd baby-tracker-api

# Copy environment settings
cp .env.development .env

# Start everything with Docker Compose
docker-compose -f docker-compose.dev.yml up -d

# Create admin account
docker-compose -f docker-compose.dev.yml exec web python manage.py createsuperuser

# Visit your app at http://localhost:8000
```

**Quick Start with Make (Recommended)**

```bash
# Clone the repository
git clone https://github.com/theamazingmrb/baby-tracker-api.git
cd baby-tracker-api

# Copy environment settings
cp .env.development .env

# Quick start (builds, starts, migrates, creates superuser)
make quick-start

# Visit your app at http://localhost:8000
```

**Docker handles everything for you:**
- Python 3.11 environment
- PostgreSQL database
- Redis caching
- All Python dependencies
- Environment configuration

#### Option 2: Manual Setup (Advanced)

If you prefer to set up without Docker, follow these steps:

**System Dependencies:**

```bash
# macOS
brew install python@3.11 postgresql redis uv
brew services start postgresql
brew services start redis
createdb babytracker_dev

# Ubuntu/Debian
sudo apt update
sudo apt install python3.11 python3.11-venv postgresql redis-server uv
sudo systemctl start postgresql
sudo systemctl start redis-server
sudo -u postgres createdb babytracker_dev

# Windows (WSL2)
sudo apt update
sudo apt install python3.11 python3.11-venv postgresql redis-server
sudo systemctl start postgresql
sudo systemctl start redis-server
sudo -u postgres createdb babytracker_dev
```

**Python Environment:**

```bash
# Create virtual environment
uv venv --python 3.11
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
uv pip install -e .
```

**Database and Django Setup:**

```bash
# Create database user (if needed)
createuser --interactive --pwprompt babytracker
psql -c "GRANT ALL PRIVILEGES ON DATABASE babytracker_dev TO babytracker;"

# Django setup
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py collectstatic --noinput
uv run python manage.py runserver

# Visit your app at http://localhost:8000
```

### Project Setup

**With Docker and Make (Recommended)**

1. **Clone the repository**
   ```bash
   git clone https://github.com/theamazingmrb/baby-tracker-api.git
   cd baby-tracker-api
   ```

2. **Configure environment**
   ```bash
   # Copy development settings
   cp .env.development .env
   # Edit .env if needed (defaults work for local testing)
   nano .env
   ```

3. **Quick start**
   ```bash
   make quick-start
   ```

4. **Visit your app** at http://localhost:8000

**Manual Docker Setup**

1. **Clone the repository**
   ```bash
   git clone https://github.com/theamazingmrb/baby-tracker-api.git
   cd baby-tracker-api
   ```

2. **Configure environment**
   ```bash
   # Copy development settings
   cp .env.development .env
   # Edit .env if needed (defaults work for local testing)
   nano .env
   ```

3. **Start with Docker Compose**
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
   ```

4. **Create admin account**
   ```bash
   docker-compose -f docker-compose.dev.yml exec web python manage.py createsuperuser
   ```

5. **Visit your app** at http://localhost:8000

**Manual Setup (Advanced)**

If you prefer to set up without Docker, follow these steps:

#### Prerequisites

```bash
# Check Python version (needs 3.11)
python --version

# Check if PostgreSQL is available
psql --version

# Check if Redis is available
redis-cli --version

# Check if UV is installed
uv --version
```

#### System Dependencies

**macOS:**
```bash
# Install dependencies
brew install python@3.11 postgresql redis uv

# Start services
brew services start postgresql
brew services start redis

# Create database
createdb babytracker_dev
```

**Ubuntu/Debian:**
```bash
# Install dependencies
sudo apt update
sudo apt install python3.11 python3.11-venv postgresql redis-server uv

# Start services
sudo systemctl start postgresql
sudo systemctl start redis-server

# Create database
sudo -u postgres createdb babytracker_dev
```

**Windows (WSL2):**
```bash
# Install in WSL2 Ubuntu
sudo apt update
sudo apt install python3.11 python3.11-venv postgresql redis-server

# Start services
sudo systemctl start postgresql
sudo systemctl start redis-server

# Create database
sudo -u postgres createdb babytracker_dev
```

#### Python Setup

```bash
# Create virtual environment
uv venv --python 3.11
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Install the package in development mode
uv pip install -e .
```

#### Database Setup

```bash
# Create database user (if needed)
createuser --interactive --pwprompt babytracker

# Grant permissions
psql -c "GRANT ALL PRIVILEGES ON DATABASE babytracker_dev TO babytracker;"

# Test connection
psql -d babytracker_dev -c "SELECT version();"
```

#### Django Setup

```bash
# Create and apply migrations
uv run python manage.py makemigrations
uv run python manage.py migrate

# Create superuser
uv run python manage.py createsuperuser

# Collect static files
uv run python manage.py collectstatic --noinput

# Start the server
uv run python manage.py runserver

# Visit your app at http://localhost:8000
```

## API Reference

### Authentication

The Baby Tracker API uses JWT (JSON Web Token) authentication. To access protected endpoints:

1. **Register a new account**
   ```bash
   curl -X POST http://localhost:8000/api/tracker/register/ \
     -H "Content-Type: application/json" \
     -d '{"username":"testuser","email":"test@example.com","password":"testpass123"}'
   ```

2. **Login to get token**
   ```bash
   curl -X POST http://localhost:8000/api/tracker/token/ \
     -H "Content-Type: application/json" \
     -d '{"username":"testuser","password":"testpass123"}'
   ```

3. **Use token in requests**
   ```bash
   curl -H "Authorization: Bearer YOUR_TOKEN" \
     http://localhost:8000/api/tracker/babies/
   ```

4. **Refresh token**
   ```bash
   curl -X POST http://localhost:8000/api/tracker/token/refresh/ \
     -H "Authorization: Bearer YOUR_REFRESH_TOKEN"
   ```

### Endpoints

| Endpoint | Method | Description | Authentication |
|----------|--------|-------------|----------------|
| `/api/tracker/register/` | POST | Register new account | None |
| `/api/tracker/token/` | POST | Login and get token | None |
| `/api/tracker/token/refresh/` | POST | Refresh JWT token | Required |
| `/api/tracker/babies/` | GET, POST | Manage baby profiles | Required |
| `/api/tracker/babies/<int:pk>/` | GET, PUT, DELETE | Manage specific baby | Required |
| `/api/tracker/babies/stats/` | GET | Get baby statistics | Required |
| `/api/tracker/feedings/` | GET, POST | Track feeding activities | Required |
| `/api/tracker/feedings/<int:pk>/` | GET, PUT, DELETE | Manage specific feeding | Required |
| `/api/tracker/diaper-changes/` | GET, POST | Track diaper changes | Required |
| `/api/tracker/diaper-changes/<int:pk>/` | GET, PUT, DELETE | Manage specific diaper change | Required |
| `/api/tracker/sleep/` | GET, POST | Track sleep sessions | Required |
| `/api/tracker/sleep/<int:pk>/` | GET, PUT, DELETE | Manage specific sleep session | Required |
| `/api/tracker/growth-milestones/` | GET, POST | Track growth milestones | Required |
| `/api/tracker/growth-milestones/<int:pk>/` | GET, PUT, DELETE | Manage specific growth milestone | Required |
| `/api/tracker/appointments/` | GET, POST | Manage doctor appointments | Required |
| `/api/tracker/appointments/<int:pk>/` | GET, PUT, DELETE | Manage specific appointment | Required |
| `/api/tracker/medications/` | GET, POST | Track medications | Required |
| `/api/tracker/medications/<int:pk>/` | GET, PUT, DELETE | Manage specific medication | Required |
| `/api/tracker/pumping-sessions/` | GET, POST | Track pumping sessions | Required |
| `/api/tracker/pumping-sessions/<int:pk>/` | GET, PUT, DELETE | Manage specific pumping session | Required |
| `/api/tracker/reminders/` | GET, POST | Manage reminders | Required |
| `/api/tracker/reminders/<int:pk>/` | GET, PUT, DELETE | Manage specific reminder | Required |
| `/api/tracker/recipes/` | GET, POST | Manage baby food recipes | Required |
| `/api/tracker/recipes/<int:pk>/` | GET, PUT, DELETE | Manage specific recipe | Required |
| `/api/tracker/ingredients/` | GET, POST | Manage recipe ingredients | Required |
| `/api/tracker/ingredients/<int:pk>/` | GET, PUT, DELETE | Manage specific ingredient | Required |
| `/api/tracker/babies/<int:baby_id>/milestones/` | GET, POST | Manage developmental milestones | Required |
| `/api/tracker/babies/<int:baby_id>/milestones/<int:pk>/` | GET, PUT, DELETE | Manage specific milestone | Required |
| `/api/tracker/babies/<int:baby_id>/ai-insights/` | GET | Get AI-powered insights | Required |
| `/api/tracker/babies/<int:baby_id>/visualizations/` | GET | Get insights visualizations | Required |

### Data Models

#### Baby
```json
{
  "id": 1,
  "name": "Emma",
  "birth_date": "2023-05-15",
  "gender": "female"
}
```

#### Feeding
```json
{
  "id": 1,
  "baby": 1,
  "time": "2023-12-01T10:30:00Z",
  "feeding_type": "breastfeeding",
  "quantity": 2.5,
  "last_side": "left"
}
```

#### Diaper Change
```json
{
  "id": 1,
  "baby": 1,
  "time": "2023-12-01T11:00:00Z",
  "diaper_type": "wet"
}
```

#### Sleep Session
```json
{
  "id": 1,
  "baby": 1,
  "start_time": "2023-12-01T20:00:00Z",
  "end_time": "2023-12-01T06:00:00Z"
}
```

#### Growth Milestone
```json
{
  "id": 1,
  "baby": 1,
  "date": "2023-12-01",
  "height": 65.0,
  "weight": 7.2,
  "notes": "Growing well!"
}
```

#### Developmental Milestone
```json
{
  "id": 1,
  "baby": 1,
  "title": "First Steps",
  "category": "physical",
  "date_achieved": "2023-12-01",
  "notes": "Took first steps today!"
}
```

#### Doctor Appointment
```json
{
  "id": 1,
  "baby": 1,
  "doctor_name": "Dr. Smith",
  "location": "Pediatric Clinic",
  "date": "2023-12-15",
  "time": "10:30:00",
  "reason": "Regular checkup",
  "notes": "All vaccinations up to date"
}
```

#### Medication
```json
{
  "id": 1,
  "user": 1,
  "name": "Vitamin D",
  "dosage": "400 IU",
  "frequency": "daily",
  "start_date": "2023-12-01",
  "end_date": null
}
```

#### Pumping Session
```json
{
  "id": 1,
  "user": 1,
  "time": "2023-12-01T09:00:00Z",
  "side": "left",
  "quantity": 3.0
}
```

#### Reminder
```json
{
  "id": 1,
  "user": 1,
  "baby": 1,
  "message": "Feeding time",
  "time": "2023-12-01T10:00:00Z"
}
```

#### Recipe
```json
{
  "id": 1,
  "name": "Sweet Potato Puree",
  "cover_image": "data:image/jpeg;base64,...",
  "description": "Nutritious and delicious",
  "instructions": "Bake sweet potato, then blend until smooth",
  "category": "baby food",
  "is_private": false
}
```

#### Ingredient
```json
{
  "id": 1,
  "name": "Sweet Potato",
  "recipe": 1,
  "quantity": 2.0,
  "unit": "cups"
}
```

## Building a Frontend

This project provides the complete backend system for baby tracking. While it doesn't include a ready-to-use mobile app, it gives you everything needed to build your own custom interface.

### Integration Example

```javascript
// Example of connecting to your baby tracking data
async function getBabyData() {
  const token = localStorage.getItem('token');
  const response = await fetch('http://your-server/api/tracker/babies/', {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  });
  return await response.json();
}

// Example of logging a feeding
async function logFeeding(babyId, feedingData) {
  const token = localStorage.getItem('token');
  const response = await fetch(`http://your-server/api/tracker/feedings/`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      baby: babyId,
      ...feedingData
    })
  });
  return await response.json();
}

// Example of getting AI insights
async function getAIInsights(babyId) {
  const token = localStorage.getItem('token');
  const response = await fetch(`http://your-server/api/tracker/babies/${babyId}/ai-insights/`, {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  });
  return await response.json();
}
```

### Mobile Considerations

Since parents are often on the go, consider building a mobile-first design that allows quick one-handed logging of activities while caring for your baby.

### Development

### Environment Variables

Key environment variables in `.env`:

```bash
# Django settings
SECRET_KEY=your-secret-key-here-change-in-production
DJANGO_DEBUG=True
ENVIRONMENT=development
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Database setup
DATABASE_URL=postgres://postgres:postgres@localhost:5432/babytracker_dev

# Redis setup
REDIS_URL=redis://127.0.0.1:6379/1

# Features
ENABLE_AI_INSIGHTS=True
ENABLE_DEBUG_TOOLBAR=True
ENABLE_RATE_LIMITING=True
```

### Development Commands

The project includes a Makefile with convenient commands:

```bash
# Show all available commands
make help

# Quick start for new setup
make quick-start

# Development workflow
make up          # Start containers
make logs        # Show logs
make shell       # Django shell
make test        # Run tests
make migrate     # Run migrations
make createsuperuser  # Create admin user

# Database management
make db-shell    # PostgreSQL shell
make reset-db    # Reset database (WARNING: deletes data)
make load-demo   # Load demo data

# Code quality
make format      # Format code
make lint        # Run linting
make check       # Run all checks

# Utilities
make status      # Show container status
make clean       # Clean up Docker resources
make info         # Show development info
```

### Testing

```bash
# Run all tests
make test

# Run with coverage
make test-coverage

# Run tests for specific app
make test-app APP=tracker
```

### Debug Tools

When `DEBUG=True`, you get access to helpful debugging tools:
- SQL query analysis
- Performance profiling  
- Request/response inspection
- Debug toolbar at http://localhost:8000/__debug__/

### Development Workflow

```bash
# Start development
make dev

# Run tests and linting
make dev-test

# Make changes and restart
make restart

# Check logs
make logs

# Database operations
make migrations
make migrate

# Create admin user
make createsuperuser
```

## Performance

### Response Times

- **Baby list**: <50ms (indexed queries)
- **Activity creation**: <100ms (cached validation)
- **AI insights**: <500ms (optimized ML pipelines)
- **Statistics**: <30ms (cached aggregations)

### Rate Limits

- **GET requests**: 100-200/hour
- **POST requests**: 1000/hour  
- **PUT requests**: 500/hour
- **DELETE requests**: 100/hour

## Deployment

### Production Setup

- Use PostgreSQL for production database
- Configure Redis for caching and rate limiting
- Set `DEBUG=False` in production
- Configure proper CORS origins
- Use environment variables for secrets
- Set up monitoring and logging

### Docker Deployment

```bash
# Build and run with Docker
docker build -t baby-tracker-api .
docker run -p 8000:8000 baby-tracker-api
```

## Security

### Multi-Tenancy

The API implements complete tenant isolation to ensure data security:

- **Permission Control**: Custom permission classes ensure users can only access their own data
- **Query Filtering**: All API endpoints filter data based on the authenticated user
- **Validation**: Serializers validate that users can only create/modify data for their own babies
- **Comprehensive Testing**: Tenant isolation is verified through extensive test coverage

### Security Features

- **HTTPS Protection**: Automatic secure connections in production
- **Security Headers**: Protection against common web attacks
- **CSRF Protection**: Built-in protection against cross-site requests
- **Secure Cookies**: Extra protection for user data in production

## Documentation

- **Interactive API Docs**: http://localhost:8000/api/docs/ (Swagger UI)
- **Clean Documentation**: http://localhost:8000/api/redoc/
- **Technical Schema**: http://localhost:8000/api/schema/
- **Admin Panel**: http://localhost:8000/admin/
- **Debug Toolbar**: http://localhost:8000/__debug__/ (when DEBUG=True)

## Contributing

1. Fork the project
2. Create a feature branch
3. Add tests for new features
4. Make sure all tests pass
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Running Tests

To run the test suite locally:

```bash
docker-compose -f docker-compose.dev.yml exec web python manage.py test
```

To run tests with coverage reporting:

```bash
docker-compose -f docker-compose.dev.yml exec web coverage run --source='.' manage.py test
docker-compose -f docker-compose.dev.yml exec web coverage report
```

### Test Structure

Tests are organized by feature and API endpoint, located in each app's `tests/` directory:

- Authentication tests
- Baby management tests
- Activity tracking tests (feeding, sleep, diaper changes, etc.)
- Recipe management tests
- AI insights tests
- Visualization tests

Each test file focuses on a specific model or feature, with comprehensive coverage of:
- CRUD operations
- Authentication and authorization
- Tenant isolation
- Input validation
- Error handling

### Continuous Integration

Tests run automatically on GitHub Actions for every push and pull request to ensure code quality and prevent regressions. The CI workflow:

1. Sets up a test environment with PostgreSQL
2. Runs the full test suite
3. Generates and reports test coverage

For more details on writing tests, see the [Testing Guide](docs/testing_guide.md).

## Project Structure

```
babytracker/          # Main Django project directory
├── settings.py       # Project settings
├── urls.py           # Main URL routing
├── views.py          # Views including landing page
└── wsgi.py           # WSGI configuration

tracker/              # Main application directory
├── ai_insights.py    # AI insights and analytics module
├── base_views.py     # Base view classes for baby/user-owned models
├── enums.py          # Enums for feeding and pumping sides
├── models.py         # Database models
├── permissions.py    # Custom permission classes
├── serializers.py    # API serializers
├── urls.py           # API URL routing
├── views.py          # API views
└── tests/            # Test directory
    ├── test_ai_insights_api.py       # Tests for AI insights
    ├── test_baby_api.py          # Tests for baby management API
    ├── test_diaper_change_api.py # Tests for diaper change API
    ├── test_doctor_appointment_api.py # Tests for doctor appointments API
    ├── test_feeding_api.py       # Tests for feeding API
    ├── test_growth_milestone_api.py # Tests for growth milestones API
    ├── test_medication_api.py    # Tests for medication API
    ├── test_milestone_api.py     # Tests for developmental milestones API
    ├── test_pumping_session_api.py # Tests for pumping sessions API
    ├── test_reminder_api.py      # Tests for reminders API
    ├── test_sleep_api.py         # Tests for sleep API
    └── test_visualization_api.py # Tests for visualization API

templates/            # HTML templates
├── index.html        # Default template
└── landing.html      # Landing page with inline styles

static/               # Static files

docs/                 # Documentation
└── testing_guide.md  # Guide for writing tests

.github/              # GitHub configuration
├── ISSUE_TEMPLATE/   # GitHub issue templates
│   ├── bug_report.md # Bug report template
│   └── feature_request.md # Feature request template
└── workflows/        # GitHub Actions workflows
    └── test.yml      # CI testing workflow
```

## Security Features

### Multi-Tenancy

This API implements complete tenant isolation to ensure data security in a multi-user environment:

- **Permission Control**: Custom `IsTenantUser` permission class ensures users can only access their own data
- **Query Filtering**: All API endpoints filter data based on the authenticated user
- **Validation**: Serializers validate that users can only create/modify data for their own babies
- **Comprehensive Testing**: Tenant isolation is verified through extensive test coverage

This multi-layered approach guarantees that users can only view and manipulate their own data, making the API safe for public deployment.

## Deployment Options

### AWS EC2 Deployment with Docker Compose (Recommended)

The easiest way to deploy Baby Tracker to production is using AWS EC2 with Docker Compose:

1. **Launch an EC2 instance**:
   - Use a t3.nano instance (sufficient for most use cases, ~$5-6/month)
   - Select Amazon Linux 2023 or Ubuntu Server
   - Configure security group to allow HTTP (port 80), HTTPS (port 443), and SSH (port 22)
   - Create or use an existing key pair for SSH access

2. **Connect to your instance**:
   ```bash
   ssh -i your-key.pem ec2-user@your-instance-ip
   ```

3. **Install Docker and Docker Compose**:
   ```bash
   # For Amazon Linux 2023
   sudo yum update -y
   sudo yum install -y docker
   sudo systemctl start docker
   sudo systemctl enable docker
   sudo usermod -aG docker $USER
   
   # Install Docker Compose
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

4. **Clone the repository**:
   ```bash
   git clone https://github.com/theamazingmrb/baby-tracker-api.git
   cd baby-tracker-api
   ```

5. **Create and configure environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your production settings
   # Make sure to set:
   # - DJANGO_DEBUG=False
   # - PRODUCTION_DOMAIN=your-domain.com
   # - ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com,www.your-domain.com
   # - CORS_ALLOWED_ORIGINS=http://your-domain.com,https://your-domain.com,http://www.your-domain.com,https://www.your-domain.com
   ```

6. **Choose your deployment option**:

   **Option A: Basic HTTP deployment**
   ```bash
   docker-compose up -d
   ```

   **Option B: HTTPS deployment with Nginx and Let's Encrypt**
   ```bash
   # Create required directories for Nginx and Certbot
   mkdir -p nginx/conf nginx/certbot/conf nginx/certbot/www
   
   # Create a basic Nginx configuration
   cat > nginx/conf/app.conf << 'EOL'
   server {
       listen 80;
       server_name your-domain.com www.your-domain.com;
       
       location /.well-known/acme-challenge/ {
           root /var/www/certbot;
       }
       
       location / {
           return 301 https://$host$request_uri;
       }
   }
   
   server {
       listen 443 ssl;
       server_name your-domain.com www.your-domain.com;
       
       ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
       
       location / {
           proxy_pass http://web:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   EOL
   
   # Replace your-domain.com with your actual domain
   sed -i 's/your-domain.com/example.com/g' nginx/conf/app.conf  # Replace example.com with your domain
   
   # Start with HTTPS configuration
   docker-compose -f docker-compose.https.yml up -d
   
   # Get SSL certificates (after DNS is properly configured)
   docker-compose -f docker-compose.https.yml exec certbot certbot certonly --webroot -w /var/www/certbot -d your-domain.com -d www.your-domain.com --email your-email@example.com --agree-tos --no-eff-email
   
   # Reload Nginx to apply the certificates
   docker-compose -f docker-compose.https.yml exec nginx nginx -s reload
   ```

7. **Create a superuser**:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

8. **Access your application** at http://your-domain.com/ (or https://your-domain.com/ if using HTTPS) and the admin interface at http://your-domain.com/admin/ (or https://your-domain.com/admin/)

### Local Docker Deployment (Recommended)

For local development or self-hosting on your own hardware:

1. Clone the repository:
   ```bash
   git clone https://github.com/theamazingmrb/baby-tracker-api.git
   cd baby-tracker-api
   ```

2. Create an `.env` file from the development template:
   ```bash
   cp .env.development .env
   # Edit .env with your settings (defaults work for local development)
   ```

3. Build and start the containers:
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
   ```

4. Create a superuser:
   ```bash
   docker-compose -f docker-compose.dev.yml exec web python manage.py createsuperuser
   ```

5. Access the application:
   - **API Documentation**: http://localhost:8000/
   - **Admin Interface**: http://localhost:8000/admin/
   - **API Endpoints**: http://localhost:8000/api/tracker/

6. Development workflow:
   ```bash
   # View logs
   docker-compose -f docker-compose.dev.yml logs -f web
   
   # Run migrations
   docker-compose -f docker-compose.dev.yml exec web python manage.py migrate
   
   # Run tests
   docker-compose -f docker-compose.dev.yml exec web python manage.py test
   
   # Stop environment
   docker-compose -f docker-compose.dev.yml down
   ```

### Custom Deployment Options

While the EC2 + Docker Compose method above is recommended for simplicity and cost-effectiveness, you can deploy Baby Tracker on any platform that supports Docker or Django:

- **Other Cloud Providers**: GCP, Azure, DigitalOcean, etc.
- **Kubernetes**: For more complex, scalable deployments
- **VPS/Dedicated Server**: Any server that can run Docker
- **Platform as a Service**: Heroku, Render, Railway, etc.

Key configuration for any production deployment:
- Use PostgreSQL database
- Configure proper environment variables (see below)
- Enable HTTPS in production
- Set up regular database backups

### Environment Variables

The following environment variables should be configured for deployment:

#### Core Django Settings
- `SECRET_KEY`: Django secret key (use a strong, random value in production)
- `DJANGO_DEBUG`: Set to 'False' in production
- `ENVIRONMENT`: Set to 'production' for production deployments
- `ALLOWED_HOSTS`: Comma-separated list of domains allowed to serve the application

#### Network Configuration
- `NETWORK_HOST`: Host to bind the Django server to (default: 0.0.0.0)
- `NETWORK_PORT`: Port for the Django server (default: 8000)
- `PRODUCTION_DOMAIN`: Your API backend domain (e.g., babytracker.xyz)

#### Database Configuration
- `DATABASE_URL`: PostgreSQL connection string
- `POSTGRES_USER`: PostgreSQL username (used by Docker)
- `POSTGRES_PASSWORD`: PostgreSQL password (used by Docker)
- `POSTGRES_DB`: PostgreSQL database name (used by Docker)

#### Redis Configuration
- `REDIS_URL`: Redis connection URL for caching and rate limiting

#### Security Settings
- `CORS_ALLOWED_ORIGINS`: Comma-separated list of origins allowed to access the API
- `CORS_ALLOW_ALL_ORIGINS`: Set to 'True' to allow all origins (not recommended for production)
- `CSRF_TRUSTED_ORIGINS`: Comma-separated list of trusted origins for CSRF

#### JWT Authentication
- `JWT_ACCESS_TOKEN_LIFETIME`: Access token lifetime in days (default: 1)
- `JWT_REFRESH_TOKEN_LIFETIME`: Refresh token lifetime in days (default: 7)

#### Logging
- `LOG_LEVEL`: Logging level (INFO, DEBUG, WARNING, ERROR)
- `LOG_FILE`: Path to log file

#### Email Configuration
- `EMAIL_BACKEND`: Email backend for sending notifications

#### Feature Flags
- `ENABLE_AI_INSIGHTS`: Enable/disable AI insights feature
- `ENABLE_DEBUG_TOOLBAR`: Enable debug toolbar in development
- `ENABLE_RATE_LIMITING`: Enable/disable API rate limiting

#### Docker/Deployment
- `WEB_PORT`: Port to expose the web service on (default: 80)

These variables should be set in your `.env` file for Docker Compose deployments.

### Production Considerations

- **Domain Setup**: To use a custom domain, configure DNS to point to your EC2 instance IP and set up Nginx or use AWS Route 53
- **HTTPS**: For production, set up SSL/TLS using Let's Encrypt with Certbot (see the HTTPS deployment option above)
- **Backups**: Set up regular PostgreSQL database backups (the database is stored in Docker volumes)
- **Monitoring**: Consider adding basic monitoring for your EC2 instance
- **Updates**: To update your application:
  ```bash
  cd baby-tracker-api
  git pull
  
  # For basic HTTP deployment
  docker-compose down
  docker-compose up -d --build
  
  # For HTTPS deployment
  docker-compose -f docker-compose.https.yml down
  docker-compose -f docker-compose.https.yml up -d --build
  ```

### Deployment Configuration Files

The project includes two Docker Compose configuration files:

1. **docker-compose.yml**: Basic deployment without HTTPS
   - Suitable for development or when using an external HTTPS proxy
   - Exposes the web service directly on port 80

2. **docker-compose.https.yml**: Production deployment with HTTPS
   - Includes Nginx as a reverse proxy and Certbot for SSL certificates
   - Handles automatic HTTPS redirection and certificate renewal
   - Recommended for production deployments

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome and greatly appreciated! Baby Tracker is a community project, and we love to have parents and developers contribute to make it better.

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on how to contribute to this project.

### Quick Start for Contributors

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas Where Help is Needed

- Frontend development (React/Vue/Angular client)
- Additional AI insights and analytics
- Mobile app development
- Translations
- Documentation improvements