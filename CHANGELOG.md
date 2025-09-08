# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2025-09-08

### Added
- Initial release of Python API/Data Starter template
- FastAPI application with health check and documentation endpoints
- JWT authentication with user registration and login
- SQLModel database models (User, Item, Payment)
- Alembic database migrations
- Background job processing with APScheduler
- Jupyter notebook for data exploration
- Docker and docker-compose configuration
- GitHub Actions CI/CD pipeline
- Comprehensive test suite
- Development scripts for common tasks
- Ruff linting and formatting
- Type checking with mypy
- Poetry dependency management

### Features
- **API Endpoints**: Health check, authentication, CRUD operations
- **Database**: SQLite/PostgreSQL support with migrations
- **Authentication**: JWT-based with password hashing
- **Background Jobs**: APScheduler integration with example jobs
- **Data Analysis**: Jupyter notebook with pandas/polars
- **Testing**: Comprehensive test suite with pytest
- **CI/CD**: GitHub Actions workflow
- **Docker**: Multi-service containerization
- **Documentation**: Comprehensive README and API docs

### Technical Stack
- FastAPI + Uvicorn
- SQLModel + SQLAlchemy + Alembic
- Pydantic v2 for validation
- JWT authentication
- APScheduler for background jobs
- Pandas/Polars for data analysis
- Docker + docker-compose
- Poetry for dependency management
- Ruff for linting/formatting
- pytest for testing
