# Baby Tracker API Makefile
# Convenient commands for development and deployment

.PHONY: help build up down restart logs shell test test-coverage migrate createsuperuser static collectstatic clean docker-clean docker-build docker-rebuild format lint check

# Default target
help: ## Show this help message
	@echo "Baby Tracker API - Available Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Development Commands
build: ## Build the Docker containers
	docker-compose -f docker-compose.dev.yml build

up: ## Start the development environment
	docker-compose -f docker-compose.dev.yml up -d

down: ## Stop the development environment
	docker-compose -f docker-compose.dev.yml down

restart: ## Restart the development environment
	docker-compose -f docker-compose.dev.yml restart

logs: ## Show development logs (follow mode)
	docker-compose -f docker-compose.dev.yml logs -f web

logs-all: ## Show all service logs
	docker-compose -f docker-compose.dev.yml logs -f

shell: ## Open Django shell in container
	docker-compose -f docker-compose.dev.yml exec web python manage.py shell

db-shell: ## Open PostgreSQL shell
	docker-compose -f docker-compose.dev.yml exec db psql -U postgres -d babytracker_dev

redis-cli: ## Open Redis CLI
	docker-compose -f docker-compose.dev.yml exec redis redis-cli

# Django Management Commands
migrate: ## Run database migrations
	docker-compose -f docker-compose.dev.yml exec web python manage.py migrate

migrations: ## Create new migration files
	docker-compose -f docker-compose.dev.yml exec web python manage.py makemigrations

createsuperuser: ## Create Django superuser
	docker-compose -f docker-compose.dev.yml exec web python manage.py createsuperuser

collectstatic: ## Collect static files
	docker-compose -f docker-compose.dev.yml exec web python manage.py collectstatic --noinput

static: collectstatic ## Alias for collectstatic

# Testing Commands
test: ## Run all tests
	docker-compose -f docker-compose.dev.yml exec web python manage.py test

test-coverage: ## Run tests with coverage report
	docker-compose -f docker-compose.dev.yml exec web coverage run --source='.' manage.py test
	docker-compose -f docker-compose.dev.yml exec web coverage report

test-app: ## Run tests for specific app (usage: make test-app APP=tracker)
	docker-compose -f docker-compose.dev.yml exec web python manage.py test $(APP)

# Code Quality Commands
format: ## Format Python code with black
	docker-compose -f docker-compose.dev.yml exec web black .

lint: ## Run code linting
	docker-compose -f docker-compose.dev.yml exec web flake8 .

check: ## Run all code quality checks (format + lint)
	$(MAKE) format
	$(MAKE) lint

# Database Commands
reset-db: ## Reset the database (WARNING: deletes all data)
	docker-compose -f docker-compose.dev.yml down -v
	docker-compose -f docker-compose.dev.yml up -d db redis
	sleep 5
	$(MAKE) migrate
	$(MAKE) createsuperuser

load-demo: ## Load demo data
	docker-compose -f docker-compose.dev.yml exec web python manage.py loaddata demo_data.json

# Production Commands
prod-build: ## Build production containers
	docker-compose build

prod-up: ## Start production environment
	docker-compose up -d

prod-down: ## Stop production environment
	docker-compose down

prod-logs: ## Show production logs
	docker-compose logs -f web

# Utility Commands
status: ## Show container status
	docker-compose -f docker-compose.dev.yml ps

ps: status ## Alias for status

clean: ## Clean up Docker resources (containers, networks, volumes)
	docker-compose -f docker-compose.dev.yml down -v --remove-orphans
	docker system prune -f

docker-clean: clean ## Alias for clean

docker-build: ## Rebuild containers from scratch
	docker-compose -f docker-compose.dev.yml build --no-cache

docker-rebuild: ## Clean and rebuild (full reset)
	$(MAKE) clean
	$(MAKE) build

# Quick Start Commands
quick-start: ## Quick start for new development setup
	$(MAKE) build
	$(MAKE) up
	sleep 10
	$(MAKE) migrate
	$(MAKE) createsuperuser
	@echo ""
	@echo "🎉 Baby Tracker API is ready!"
	@echo "📖 API Docs: http://localhost:8000/api/docs/"
	@echo "🔧 Admin Panel: http://localhost:8000/admin/"
	@echo "🐳 Container Status: make status"

fresh-start: ## Completely fresh start (cleans everything)
	$(MAKE) clean
	$(MAKE) quick-start

# Development Workflow Commands
dev: ## Start development environment with logs
	$(MAKE) up
	$(MAKE) logs

dev-test: ## Run tests in development
	$(MAKE) test
	$(MAKE) lint

# Info Commands
info: ## Show useful development information
	@echo "Baby Tracker API Development Info:"
	@echo "================================"
	@echo "🌐 API Documentation: http://localhost:8000/api/docs/"
	@echo "🔧 Django Admin: http://localhost:8000/admin/"
	@echo "📊 Debug Toolbar: http://localhost:8000/__debug__/"
	@echo "🗄️  Database: PostgreSQL on port 5432"
	@echo "🔴 Redis: Redis on port 6379"
	@echo "📝 Logs: make logs"
	@echo "🐚 Shell: make shell"
	@echo ""
	@echo "Quick Commands:"
	@echo "  make quick-start    - Set up everything from scratch"
	@echo "  make dev             - Start development with logs"
	@echo "  make test            - Run tests"
	@echo "  make createsuperuser - Create admin user"
	@echo "  make info            - Show this information"
