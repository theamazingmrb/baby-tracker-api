# Contributing to Baby Tracker

Thank you for considering contributing to Baby Tracker! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How Can I Contribute?

### Reporting Bugs

Before submitting a bug report:
- Check the issue tracker to see if the bug has already been reported
- Collect information about the bug (steps to reproduce, expected vs. actual behavior)

When submitting a bug report:
- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Explain the behavior you observed and what you expected to happen
- Include screenshots if applicable
- Include details about your environment (OS, browser, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:
- Use a clear and descriptive title
- Provide a detailed description of the suggested enhancement
- Explain why this enhancement would be useful to most Baby Tracker users

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure they pass (`python manage.py test`)
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

#### Pull Request Guidelines

- Update the README.md with details of changes if applicable
- Update the documentation if needed
- The PR should work for Python 3.8+
- Include tests for new functionality
- Maintain code style consistency

## Development Setup

1. Clone your fork of the repository
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
6. Run tests to ensure everything is working:
   ```bash
   python manage.py test
   ```

## Styleguides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Python Styleguide

- Follow PEP 8 style guidelines
- Use docstrings for functions and classes
- Write descriptive variable names

### Testing Styleguide

#### General Testing Guidelines

- Include tests for all new features and API endpoints
- Maintain or increase test coverage (aim for >90% coverage)
- Make sure all tests pass before submitting a PR
- Use descriptive test method names that explain what is being tested
- Each test should focus on a single aspect of functionality

#### API Test Structure

API tests should follow this structure:

```python
class YourFeatureAPITestCase(TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username='testuser1', password='password1')
        self.user2 = User.objects.create_user(username='testuser2', password='password2')
        
        # Create test data
        self.baby1 = Baby.objects.create(name='Baby One', user=self.user1, ...)
        
        # Setup API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        self.unauthenticated_client = APIClient()
    
    def test_list_endpoint(self):
        # Test authenticated owner can list their own records
        # Test records are properly filtered by owner
        # Test pagination if applicable
    
    def test_create_endpoint(self):
        # Test successful creation with valid data
        # Test validation errors with invalid data
        # Test authentication and authorization
    
    def test_retrieve_endpoint(self):
        # Test owner can retrieve their own records
        # Test non-owners cannot access others' records
    
    def test_update_endpoint(self):
        # Test full and partial updates
        # Test validation and authorization
    
    def test_delete_endpoint(self):
        # Test deletion removes the record
        # Test authorization controls
```

#### Test Coverage Requirements

For each API endpoint, tests should cover:

1. **Authentication**: Verify that endpoints require authentication when appropriate
2. **Authorization**: Verify that users can only access their own data
3. **Input Validation**: Test with valid and invalid inputs
4. **Success Cases**: Verify correct behavior for valid requests
5. **Error Cases**: Verify appropriate error responses for invalid requests
6. **Edge Cases**: Test boundary conditions and special cases

#### Using Mocks

When testing components that rely on external services (like AI insights):

```python
@patch('tracker.views.generate_ai_insights')
def test_ai_insights_endpoint(self, mock_generate_ai_insights):
    # Configure the mock
    mock_generate_ai_insights.return_value = {...}
    
    # Test the endpoint
    url = reverse('ai-insights', kwargs={'pk': self.baby1.id})
    response = self.client1.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
```

#### Running Tests

Run the full test suite:
```bash
python manage.py test
```

Run tests for a specific app:
```bash
python manage.py test tracker
```

Run a specific test class:
```bash
python manage.py test tracker.tests.test_baby_api.BabyAPITestCase
```

Run with coverage:
```bash
coverage run --source='.' manage.py test
coverage report
```

For more detailed information, see the [Testing Guide](docs/testing_guide.md).

## Additional Notes

### Issue and Pull Request Labels

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements or additions to documentation
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention is needed

Thank you for contributing to Baby Tracker!
