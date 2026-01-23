# Baby Tracker API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-4.2.10-green.svg)](https://www.djangoproject.com/)
[![UV](https://img.shields.io/badge/UV-lightning__fast__package__manager-purple.svg)](https://github.com/astral-sh/uv)

A production-grade API for tracking baby activities including feedings, diapers, sleep, growth milestones, and more. Built with Django REST Framework and optimized for performance and security.

## 🚀 Production-Ready Baby Tracking Solution

Baby Tracker is a privacy-first, self-hostable solution that gives parents complete control over their baby's data. Features enterprise-grade optimizations including rate limiting, caching, structured logging, and database indexing for optimal performance.

## ✨ Key Features

### Core Functionality
- **Baby Management**: Create and manage baby profiles
- **Activity Tracking**:
  - Feedings (breastfeeding, bottle, solid food)
  - Diaper changes
  - Sleep sessions
  - Growth milestones
  - Doctor appointments
  - Medications
  - Pumping sessions
- **AI Insights**: Get recommendations for feeding times and sleep patterns based on historical data
- **Recipe Management**: Store and manage baby food recipes
- **JWT Authentication**: Secure API access with token-based authentication

### Production Features
- **🔒 Security Hardening**: XSS protection, secure headers, HTTPS enforcement
- **⚡ Rate Limiting**: User-based rate limiting (100-1000 requests/hour)
- **🗄️ Database Optimization**: Strategic indexing for lightning-fast queries
- **📊 Structured Logging**: Comprehensive logging with file and console output
- **💾 Redis Caching**: High-performance caching layer
- **🛡️ Permission System**: Robust user/baby ownership validation
- **📈 Monitoring Ready**: Debug toolbar and observability features

## 🛠 Tech Stack

### Backend
- **Framework**: Django 4.2.10 + Django REST Framework 3.14.0
- **Package Manager**: UV (10-100x faster than pip)
- **Database**: PostgreSQL with optimized indexing
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Documentation**: OpenAPI 3.0 (drf-spectacular)
- **Data Analysis**: Pandas, NumPy, SciPy, Scikit-learn
- **Caching**: Redis
- **Rate Limiting**: django-ratelimit
- **Security**: django-cors-headers, security middleware

### Development Tools
- **Debug Toolbar**: django-debug-toolbar for development
- **Configuration**: python-decouple for environment management
- **Logging**: Structured logging with rotation
- **Testing**: Django test framework with coverage support

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/babies/` | Baby management |
| `/api/feedings/` | Feeding tracking |
| `/api/diaper-changes/` | Diaper change tracking |
| `/api/sleep/` | Sleep tracking |
| `/api/growth-milestones/` | Growth milestone tracking |
| `/api/appointments/` | Doctor appointment management |
| `/api/medications/` | Medication tracking |
| `/api/milestones/` | Developmental milestone tracking |
| `/api/pumping-sessions/` | Breast milk pumping tracking |
| `/api/reminders/` | Reminder management |
| `/api/recipes/` | Baby food recipe management |
| `/api/ai-insights/` | AI-powered insights and recommendations |
| `/api/auth/` | Authentication endpoints |
| `/api/token/` | JWT token authentication |

## Building a Custom Frontend

This project provides a robust API but does not include a user-facing frontend application for tracking babies. The included Next.js application serves as documentation only. To create a functional baby tracking application, you'll need to build your own frontend.

### Getting Started with a Custom Frontend

1. **Choose a Framework**: React, Vue, Angular, or any other frontend framework
2. **Authentication**: Implement JWT authentication flow using the `/api/auth/` endpoints
3. **Core Features**: Build UI components for:
   - Baby profiles
   - Feeding tracking
   - Diaper change logging
   - Sleep tracking
   - Growth milestone recording
   - Doctor appointment management

### API Integration Example

```javascript
// Example React code for fetching baby data
async function fetchBabies() {
  const token = localStorage.getItem('token');
  const response = await fetch('http://your-api-url/api/babies/', {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  });
  return await response.json();
}
```

### Mobile Considerations

Consider building a mobile-first interface or even a native mobile app, as parents often need to log events quickly on mobile devices while caring for their baby.

## 🚀 Complete Setup Guide (From Scratch)

### 📋 Prerequisites Checklist

Before starting, ensure you have these installed:

```bash
# Check Python version (requires 3.11)
python --version

# Check if Redis is installed
redis-cli --version

# Check if PostgreSQL is installed
psql --version

# Check if UV is installed
uv --version
```

### 🔧 System Dependencies Installation

#### **macOS**
```bash
# Install system dependencies
brew install python@3.11 postgresql redis uv

# Start services
brew services start postgresql
brew services start redis

# Create database
createdb babytracker_dev
```

#### **Ubuntu/Debian**
```bash
# Install system dependencies
sudo apt update
sudo apt install python3.11 python3.11-venv postgresql redis-server uv

# Start services
sudo systemctl start postgresql
sudo systemctl start redis-server

# Create database
sudo -u postgres createdb babytracker_dev
```

#### **Windows (WSL2)**
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

### 🏗️ Project Setup (Step-by-Step)

#### **1. Clone and Navigate**
```bash
git clone https://github.com/theamazingmrb/baby-tracker-api.git
cd baby-tracker-api
```

#### **2. Install UV Package Manager**
```bash
# If not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify installation
uv --version
```

#### **3. Create Virtual Environment**
```bash
# Create Python 3.11 environment
uv venv --python 3.11

# Activate environment
source .venv/bin/activate  # Linux/macOS
# On Windows: .venv\Scripts\activate
```

#### **4. Install Dependencies**
```bash
# Lightning fast installation with UV
uv pip install -r requirements.txt

# Verify installation
uv run python --version
uv run django-admin --version
```

#### **5. Setup Environment Variables**
```bash
# Copy environment template
cp .env.example .env

# Edit .env file (required changes below)
nano .env  # or use your preferred editor
```

**Critical .env settings you MUST change:**
```bash
# Django Core Settings
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
ENVIRONMENT=development
ALLOWED_HOSTS=localhost,127.0.0.1

# Network Configuration
NETWORK_HOST=0.0.0.0
NETWORK_PORT=8000

# Database Configuration
DATABASE_URL=postgres://postgres:postgres@localhost:5432/babytracker_dev

# Redis Configuration (Required for rate limiting and caching)
REDIS_URL=redis://127.0.0.1:6379/1

# Security Settings
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080,http://127.0.0.1:3000
CSRF_TRUSTED_ORIGINS=http://localhost:3000,http://localhost:8080

# JWT Authentication Settings
JWT_ACCESS_TOKEN_LIFETIME=1
JWT_REFRESH_TOKEN_LIFETIME=7

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=logs/babytracker.log

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Feature Flags
ENABLE_AI_INSIGHTS=True
ENABLE_DEBUG_TOOLBAR=True
ENABLE_RATE_LIMITING=True
```

#### **6. Database Setup**
```bash
# Create database user (if needed)
sudo -u postgres createuser --interactive --pwprompt babytracker

# Grant permissions
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE babytracker_dev TO babytracker;"

# Test connection
uv run python manage.py dbshell --command "SELECT version();"
```

#### **7. Run Django Migrations**
```bash
# Create and apply migrations
uv run python manage.py makemigrations
uv run python manage.py migrate

# Verify tables created
uv run python manage.py dbshell --command "\dt"
```

#### **8. Create Superuser**
```bash
# Create admin user
uv run python manage.py createsuperuser

# Follow prompts to create username/password
```

#### **9. Collect Static Files**
```bash
# Create static files directory
uv run python manage.py collectstatic --noinput
```

#### **10. Start Development Server**
```bash
# Start the server
uv run python manage.py runserver

# Server will be available at http://localhost:8000
```

### ✅ Verification Checklist

After setup, verify everything works:

```bash
# [ ] Server starts without errors
curl http://localhost:8000/api/

# [ ] Database connection works
uv run python manage.py dbshell --command "SELECT 1;"

# [ ] Redis connection works
redis-cli ping

# [ ] Admin panel accessible
curl http://localhost:8000/admin/

# [ ] API docs accessible
curl http://localhost:8000/api/docs/

# [ ] Debug toolbar visible (if DEBUG=True)
# Visit http://localhost:8000/admin/ and look for debug toolbar
```

### 🔧 Common Setup Issues & Solutions

#### **PostgreSQL Connection Issues**
```bash
# Check if PostgreSQL is running
brew services list | grep postgresql  # macOS
sudo systemctl status postgresql     # Linux

# Reset PostgreSQL password
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'newpassword';"
```

#### **Redis Connection Issues**
```bash
# Check if Redis is running
redis-cli ping

# Start Redis manually
redis-server

# Check Redis logs
tail -f /usr/local/var/log/redis.log  # macOS
```

#### **Python/UV Issues**
```bash
# Recreate virtual environment
rm -rf .venv
uv venv --python 3.11
source .venv/bin/activate
uv pip install -r requirements.txt
```

#### **Permission Issues**
```bash
# Fix log directory permissions
mkdir -p logs
chmod 755 logs

# Fix static files directory
mkdir -p staticfiles
chmod 755 staticfiles
```

### 🎯 Quick Test Commands

```bash
# Test API endpoints
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"testpass123"}'

# Test authentication
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'

# Test rate limiting (should work)
for i in {1..5}; do
  curl http://localhost:8000/api/babies/
done
```

### 🚀 Next Steps After Setup

1. **Explore API Documentation**: Visit http://localhost:8000/api/docs/
2. **Create Test Data**: Use admin panel at http://localhost:8000/admin/
3. **Run Tests**: `uv run python manage.py test`
4. **Check Logs**: `tail -f logs/babytracker.log`
5. **Monitor Redis**: `redis-cli monitor`

### 📱 Development Workflow

```bash
# Daily development workflow
source .venv/bin/activate
uv run python manage.py runserver

# In another terminal - run tests
uv run python manage.py test

# Check logs
tail -f logs/babytracker.log

# Monitor Redis
redis-cli monitor
```

## 🔧 Development Features

### Debug Toolbar
When `DEBUG=True`, the Django Debug Toolbar is available for:
- SQL query analysis
- Performance profiling
- Request/response inspection

### Structured Logging
Logs are written to both console and `logs/babytracker.log`:
```python
import logging
logger = logging.getLogger(__name__)
logger.info("User action completed", extra={'user_id': request.user.id})
```

### Rate Limiting
API endpoints are rate-limited per user:
- **GET requests**: 100-200/hour
- **POST requests**: 1000/hour  
- **PUT requests**: 500/hour
- **DELETE requests**: 100/hour

### Database Optimization
The API includes strategic database indexing for optimal performance:
- **User-based queries**: Indexed on `user_id` fields
- **Time-based queries**: Indexed on `time` and `date` fields  
- **Composite indexes**: Multi-field indexes for common query patterns
- **Foreign key optimization**: All foreign keys are indexed

### Security Features
- **HTTPS Enforcement**: Automatic redirect to HTTPS in production
- **Secure Headers**: XSS protection, content type sniffing protection
- **CSRF Protection**: Built-in Django CSRF middleware
- **Secure Cookies**: HttpOnly and Secure flags in production

## 📊 Performance Metrics

### Response Times (with optimizations)
- **Baby list**: <50ms (indexed queries)
- **Activity creation**: <100ms (cached validation)
- **AI insights**: <500ms (optimized ML pipelines)
- **Statistics**: <30ms (cached aggregations)

### Rate Limits
- **Burst capacity**: 1000 requests/hour for writes
- **Sustained rate**: 200 requests/hour for reads
- **Per-user isolation**: Limits don't affect other users

## 🧪 Testing

Run the comprehensive test suite:
```bash
# Run all tests
uv run python manage.py test

# Run with coverage
uv run coverage run --source='.' manage.py test
uv run coverage report
```

## 📝 API Documentation

- **Interactive Docs**: http://localhost:8000/api/docs/ (Swagger UI)
- **ReDoc**: http://localhost:8000/api/redoc/
- **OpenAPI Schema**: http://localhost:8000/api/schema/
- **Admin Panel**: http://localhost:8000/admin/

## 🚀 Deployment

### Production Considerations
- Use PostgreSQL for production database
- Configure Redis for caching and rate limiting
- Set `DEBUG=False` in production
- Configure proper CORS origins
- Use environment variables for secrets
- Set up monitoring and logging

### Docker Support
```bash
# Build and run with Docker
docker build -t baby-tracker-api .
docker run -p 8000:8000 baby-tracker-api
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Running Tests

To run the test suite locally:

```bash
python manage.py test
```

To run tests with coverage reporting:

```bash
coverage run --source='.' manage.py test
coverage report
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
├── models.py         # Database models
├── permissions.py    # Custom permission classes
├── serializers.py    # API serializers
├── urls.py           # API URL routing
├── views.py          # API views
└── tests/            # Test directory
    ├── test_ai_insights.py       # Tests for AI insights
    ├── test_ai_insights_api.py   # Tests for AI insights API
    ├── test_baby_api.py          # Tests for baby management API
    ├── test_baby_stats_api.py    # Tests for baby statistics API
    ├── test_diaper_change_api.py # Tests for diaper change API
    ├── test_doctor_appointment_api.py # Tests for doctor appointments API
    ├── test_feeding_api.py       # Tests for feeding API
    ├── test_growth_milestone_api.py # Tests for growth milestones API
    ├── test_medication_api.py    # Tests for medication API
    ├── test_milestone_api.py     # Tests for milestones API
    ├── test_permissions.py       # Tests for permissions
    ├── test_pumping_session_api.py # Tests for pumping sessions API
    ├── test_reminder_api.py      # Tests for reminders API
    ├── test_serializers.py       # Tests for serializers
    ├── test_sleep_api.py         # Tests for sleep API
    ├── test_tenant_isolation.py  # Tests for tenant isolation
    └── test_visualization_api.py # Tests for visualization API

recipes/              # Recipe management app
├── models.py         # Recipe models
├── serializers.py    # Recipe serializers
├── views.py          # Recipe views
└── tests/            # Recipe tests
    └── test_recipe_api.py        # Tests for recipe API

frontend/             # Next.js documentation site
├── public/           # Static assets
├── src/              # Source code
│   ├── app/          # Next.js app directory
│   │   ├── api-docs/       # API documentation page
│   │   ├── contribute/     # Contribution guide page
│   │   ├── deployment-guide/ # Deployment guide page
│   │   ├── setup-guide/    # Setup guide page
│   │   ├── testing-guide/  # Testing guide page
│   │   └── page.tsx        # Home page
│   ├── components/   # React components
│   │   ├── ApiSection.tsx        # API documentation component
│   │   ├── ContributeSection.tsx # Contribution guide component
│   │   ├── DeploymentSection.tsx # Deployment guide component
│   │   ├── Header.tsx            # Header component
│   │   ├── SetupSection.tsx      # Setup guide component
│   │   └── TestingGuideSection.tsx # Testing guide component
│   └── styles/       # CSS styles

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
   # - FRONTEND_DOMAIN=your-domain.com
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

### Local Docker Deployment

For local development or self-hosting on your own hardware:

1. Clone the repository:
   ```bash
   git clone https://github.com/theamazingmrb/baby-tracker-api.git
   cd baby-tracker-api
   ```

2. Create an `.env` file from the example:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. Build and start the containers:
   ```bash
   docker-compose up -d
   ```

4. Create a superuser:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. Access the API at http://localhost:80/api/ and admin interface at http://localhost:80/admin/

### Documentation Site Deployment

The project includes a Next.js documentation site that can be deployed separately:

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Build the documentation site:
   ```bash
   npm run build
   ```

4. Start the documentation server:
   ```bash
   npm start
   ```

5. Access the documentation at http://localhost:3000/

Alternatively, you can deploy the documentation site to a service like Vercel or Netlify for production use.

**Note**: This frontend is for documentation purposes only and does not provide a user interface for the baby tracking functionality. Developers using this API would need to build their own frontend application to interact with the API endpoints.

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

- `PRODUCTION_DOMAIN`: Your API backend domain (e.g., babytracker.xyz or EC2 IP address)
- `FRONTEND_DOMAIN`: Your frontend application domain (e.g., babytracker.xyz)
- `ALLOWED_HOSTS`: Comma-separated list of domains allowed to serve the application (e.g., localhost,127.0.0.1,babytracker.xyz,www.babytracker.xyz)
- `CORS_ALLOWED_ORIGINS`: Comma-separated list of origins allowed to access the API (should include both HTTP and HTTPS versions of your domains)
- `CORS_ALLOW_ALL_ORIGINS`: Set to 'True' to allow all origins (not recommended for production)
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Django secret key (use a strong, random value)
- `DJANGO_DEBUG`: Set to 'False' in production
- `POSTGRES_USER`: PostgreSQL username (used by Docker)
- `POSTGRES_PASSWORD`: PostgreSQL password (used by Docker)
- `POSTGRES_DB`: PostgreSQL database name (used by Docker)
- `WEB_PORT`: Port to expose the web service on (default: 80)
- `NETWORK_HOST`: Host to bind the Django server to (default: 0.0.0.0)
- `NETWORK_PORT`: Port for the Django server (default: 8000)

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
