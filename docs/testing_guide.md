# Baby Tracker Testing Guide

This guide provides instructions for writing and running tests for the Baby Tracker application.

## Table of Contents

1. [Testing Framework](#testing-framework)
2. [Test Structure](#test-structure)
3. [Running Tests](#running-tests)
4. [Writing API Tests](#writing-api-tests)
5. [Mocking](#mocking)
6. [CI Integration](#ci-integration)

## Testing Framework

The Baby Tracker application uses Django's built-in testing framework along with Django REST Framework's testing utilities. Key components include:

- `django.test.TestCase`: Base class for Django tests
- `rest_framework.test.APIClient`: Client for making API requests in tests
- `unittest.mock`: For mocking external dependencies

## Test Structure

Tests are organized by feature/model and placed in the appropriate app's `tests` directory:

- `tracker/tests/`: Tests for the tracker app
- `recipes/tests/`: Tests for the recipes app

Each test file should focus on a specific model or feature, with class names following the pattern `{Feature}APITestCase`.

## Running Tests

### Running All Tests

```bash
python manage.py test
```

### Running Tests for a Specific App

```bash
python manage.py test tracker
```

### Running a Specific Test Class

```bash
python manage.py test tracker.tests.test_baby_api.BabyAPITestCase
```

### Running with Coverage

```bash
coverage run --source='.' manage.py test
coverage report
```

## Writing API Tests

### Test Setup

Each API test class should:

1. Create test users in the `setUp` method
2. Create necessary model instances for testing
3. Set up API clients for authenticated and unauthenticated requests

Example:

```python
def setUp(self):
    # Create test users
    self.user1 = User.objects.create_user(
        username='testuser1',
        email='test1@example.com',
        password='testpassword1'
    )
    
    # Create test data
    self.baby1 = Baby.objects.create(
        name='Baby One',
        birth_date='2023-01-01',
        gender='Male',
        user=self.user1
    )
    
    # Setup API clients
    self.client1 = APIClient()
    self.client1.force_authenticate(user=self.user1)
    self.unauthenticated_client = APIClient()
```

### Test Methods

For each endpoint, test:

1. Successful operations by authenticated owners
2. Unauthorized access by non-owners
3. Unauthenticated access
4. Input validation
5. Error handling

Example test method:

```python
def test_create_feeding(self):
    """Test creating a new feeding record"""
    url = reverse('feeding-list')
    data = {
        'baby': self.baby1.id,
        'start_time': '2023-01-01T08:00:00Z',
        'end_time': '2023-01-01T08:30:00Z',
        'type': 'bottle',
        'amount': 120,
        'unit': 'ml',
        'notes': 'Test feeding'
    }
    
    # Test authenticated owner can create
    response = self.client1.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    # Test unauthenticated user cannot create
    response = self.unauthenticated_client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
```

### Testing Patterns

#### Testing List Endpoints

- Test that owners can list their own records
- Test that records are properly filtered by owner
- Test pagination if applicable
- Test filtering and sorting if applicable

#### Testing Create Endpoints

- Test successful creation with valid data
- Test validation errors with invalid data
- Test authentication and authorization

#### Testing Retrieve/Update/Delete Endpoints

- Test that owners can access their own records
- Test that non-owners cannot access others' records
- Test partial updates work correctly
- Test deletion removes the record

## Mocking

Use `unittest.mock.patch` to mock external services or complex functions:

```python
@patch('tracker.views.generate_ai_insights')
def test_ai_insights_endpoint(self, mock_generate_ai_insights):
    # Mock the AI insights generation function
    mock_insights = {
        "feeding_insights": "Baby is feeding well...",
    }
    mock_generate_ai_insights.return_value = mock_insights
    
    # Test the endpoint
    url = reverse('ai-insights', kwargs={'pk': self.baby1.id})
    response = self.client1.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
```

## CI Integration

Tests are automatically run in GitHub Actions on every push to main and on pull requests. The workflow:

1. Sets up a PostgreSQL database
2. Installs dependencies
3. Runs all tests
4. Generates and uploads a coverage report

To see test results, check the Actions tab in the GitHub repository.

If a test fails in CI but passes locally, check for:
- Environment differences
- Database configuration
- Timezone issues
- Race conditions

## Best Practices

1. **Isolation**: Each test should be independent and not rely on other tests
2. **Realistic Data**: Use realistic test data that mimics production scenarios
3. **Comprehensive Coverage**: Test both success and failure cases
4. **Clean Setup/Teardown**: Properly set up and clean up test data
5. **Descriptive Names**: Use clear, descriptive test method names
6. **Assertions**: Make specific assertions about the expected outcomes
7. **Timezone Awareness**: Use `pytz.UTC` for datetime objects to avoid timezone issues
8. **Ownership Validation**: Always test that users can only access their own data
