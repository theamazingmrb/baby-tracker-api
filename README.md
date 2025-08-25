# Baby Tracker API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive API for tracking baby activities including feedings, diapers, sleep, growth milestones, and more. Built with Django REST Framework.

## 🚀 Open Source Baby Tracking Solution

Baby Tracker is a privacy-first, self-hostable solution that gives parents complete control over their baby's data. Track all aspects of your baby's development and get AI-powered insights to help establish healthy routines.

## Features

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
- **Multi-Tenancy**: Complete tenant isolation ensures users can only access their own data

## Tech Stack

### Backend
- **Framework**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Documentation**: OpenAPI (via drf-spectacular)
- **Data Analysis**: Pandas for AI insights

### Documentation Frontend
- **Framework**: Next.js with React
- **Styling**: Tailwind CSS
- **Purpose**: Interactive API and project documentation
- **Responsive Design**: Mobile-first approach

**Note**: This frontend serves as documentation and does not provide a user interface for tracking babies. It's designed to help developers understand the API and project structure.

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

## Getting Started

### Demo Configuration

Want to try Baby Tracker without setting up a full environment? Use our demo configuration:

```bash
docker-compose -f docker-compose.demo.yml up -d
```

This will start a pre-configured instance with sample data at http://localhost:8000/api/
- Demo username: `demo`
- Demo password: `babytracker123`

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/theamazingmrb/baby-tracker-api.git
   cd baby-tracker-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials and settings
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the API at http://localhost:8000/api/ and admin interface at http://localhost:8000/admin/

## API Documentation

API documentation is available at `/api/schema/` endpoint. You can view the interactive documentation by visiting `/api/schema/swagger-ui/` or `/api/schema/redoc/` in your browser.

## Landing Page

The project includes a responsive landing page that showcases the Baby Tracker features and provides links to documentation. The landing page is implemented using HTML with inline CSS for simplicity and reliability, avoiding external CSS file dependencies.

### Key Features of the Landing Page:

- Responsive design that works on mobile and desktop
- Feature showcase with icons and descriptions
- Links to API documentation
- GitHub repository links
- Simple navigation to different sections

The landing page is served by Django at the root URL (`/`) and is the first thing users see when accessing the application.

## Testing

Baby Tracker has comprehensive test coverage for all API endpoints to ensure functionality and security.

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

### Docker Deployment (Recommended)

The easiest way to deploy Baby Tracker is using Docker and docker-compose:

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

5. Access the API at http://localhost:8000/api/ and admin interface at http://localhost:8000/admin/

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

### Manual Deployment

The application can also be deployed on any platform that supports Django:

- **Heroku**: Configured for easy deployment with PostgreSQL
- **AWS/GCP/Azure**: Can be deployed as a containerized application
- **VPS/Dedicated Server**: Follow standard Django deployment practices

Key configuration for production:
- Use PostgreSQL database
- Configure WhiteNoise for static files
- Set proper environment variables
- Use HTTPS in production

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
