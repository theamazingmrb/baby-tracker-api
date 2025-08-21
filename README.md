# Baby Tracker API

A comprehensive API for tracking baby activities including feedings, diapers, sleep, growth milestones, and more. Built with Django REST Framework.

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

## Tech Stack

- **Framework**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Documentation**: OpenAPI (via drf-spectacular)
- **Data Analysis**: Pandas for AI insights

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
| `/api/pumping-sessions/` | Breast milk pumping sessions |
| `/api/babies/ai-insights/` | AI-powered insights on baby patterns |
| `/api/recipes/recipes/` | Baby food recipes |
| `/api/token/` | JWT token authentication |

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd baby-tracker-backend
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

## Deployment

The application is configured for deployment on Heroku with the following features:
- PostgreSQL database
- WhiteNoise for static files
- Environment variable configuration

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
