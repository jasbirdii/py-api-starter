# Python API/Data Starter

A comprehensive FastAPI starter template with background jobs, data analysis capabilities, and Jupyter notebooks. Perfect for APIs, data services, ETL/ELT, background jobs, analytics, and ML experiments.

## 🚀 Features

- **FastAPI** with Uvicorn for high-performance APIs
- **SQLModel/SQLAlchemy** with PostgreSQL (or SQLite for local development)
- **Alembic** for database migrations
- **Pydantic v2** for settings and data validation
- **JWT Authentication** with OAuth2
- **Background Jobs** with APScheduler (or Celery + Redis)
- **Data Analysis** with Pandas and Polars
- **Jupyter Notebooks** for exploration and analysis
- **Docker** and docker-compose for containerization
- **GitHub Actions CI** for automated testing
- **Ruff** for linting and formatting
- **pytest** for testing
- **mypy** for type checking

## 📁 Project Structure

```
py-api/
├── .env.example                 # Environment variables template
├── .github/workflows/ci.yml     # GitHub Actions CI
├── alembic.ini                  # Alembic configuration
├── docker-compose.yml           # Docker Compose setup
├── Dockerfile                   # Docker configuration
├── pyproject.toml              # Poetry dependencies and config
├── README.md                   # This file
├── scripts/                    # Development scripts
│   ├── dev.sh                  # Start development server
│   ├── lint.sh                 # Run linting and formatting
│   └── test.sh                 # Run tests
├── app/                        # Main application
│   ├── __init__.py
│   ├── main.py                 # FastAPI app
│   ├── config.py               # Settings via Pydantic
│   ├── db.py                   # Database engine and session
│   ├── dependencies.py         # FastAPI dependencies
│   ├── models.py               # SQLModel models
│   ├── schemas.py              # Pydantic schemas
│   ├── routers/                # API routers
│   │   ├── __init__.py
│   │   ├── auth.py             # Authentication endpoints
│   │   └── items.py            # Items CRUD endpoints
│   └── services/               # Business logic
│       ├── __init__.py
│       ├── payments.py         # Stripe integration
│       └── tasks.py            # Background jobs
├── migrations/                 # Alembic migrations
│   ├── env.py
│   └── script.py.mako
├── notebooks/                  # Jupyter notebooks
│   └── exploration.ipynb       # Data exploration example
└── data/                       # Data directory (gitignored)
    └── .gitignore
```

## 🛠️ Quick Start

### Prerequisites

- Python 3.11+
- Poetry (or pip)
- Docker and Docker Compose (optional)

### Local Development (SQLite)

1. **Clone and setup:**
   ```bash
   git clone <your-repo>
   cd py-api
   cp env.example .env
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

3. **Run database migrations:**
   ```bash
   alembic upgrade head
   ```

4. **Start development server:**
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

5. **Access the API:**
   - API: http://localhost:8000
   - Docs: http://localhost:8000/docs
   - Health: http://localhost:8000/health

### Docker Development (PostgreSQL)

1. **Start services:**
   ```bash
   docker-compose up --build
   ```

2. **Run migrations:**
   ```bash
   docker-compose exec api alembic upgrade head
   ```

3. **Access services:**
   - API: http://localhost:8000
   - Jupyter: http://localhost:8888
   - PostgreSQL: localhost:5432
   - Redis: localhost:6379

## 🔧 Configuration

### Environment Variables

Copy `env.example` to `.env` and configure:

```bash
# Environment
ENV=local

# Database
DATABASE_URL=sqlite:///./dev.db
# For PostgreSQL: postgresql://postgres:postgres@localhost:5432/app

# JWT
JWT_SECRET=your-super-secret-jwt-key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

# External Services
STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key
REDIS_URL=redis://localhost:6379/0

# API
API_V1_STR=/api/v1
PROJECT_NAME=Py API Starter
```

## 📊 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login user
- `GET /api/v1/auth/me` - Get current user

### Items
- `GET /api/v1/items/` - List items
- `POST /api/v1/items/` - Create item
- `GET /api/v1/items/{id}` - Get item
- `PUT /api/v1/items/{id}` - Update item
- `DELETE /api/v1/items/{id}` - Delete item

### Health
- `GET /health` - Health check

## 🔄 Background Jobs

The template includes APScheduler for background jobs. Jobs are defined in `app/services/tasks.py`:

- **Cleanup job**: Runs every 5 minutes
- **Daily report**: Runs at midnight
- **Health check**: Runs every hour

To use Celery instead, set `USE_CELERY=true` in your environment and configure Redis.

## 📓 Jupyter Notebooks

Start Jupyter Lab for data exploration:

```bash
# Local
poetry run jupyter lab

# Docker
docker-compose up jupyter
```

Access at http://localhost:8888

The `notebooks/exploration.ipynb` demonstrates:
- Database connection
- Data analysis with Pandas and Polars
- Data visualization
- API testing
- Data export

## 🧪 Development Scripts

```bash
# Start development server
./scripts/dev.sh

# Run linting and formatting
./scripts/lint.sh

# Run tests
./scripts/test.sh
```

## 🐳 Deployment

### Fly.io

1. **Install Fly CLI:**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Deploy:**
   ```bash
   fly launch
   fly deploy
   ```

3. **Add PostgreSQL:**
   ```bash
   fly postgres create
   fly secrets set DATABASE_URL="postgresql://..."
   ```

### Railway

1. Connect your GitHub repository
2. Set environment variables
3. Deploy automatically on push

### Render

1. Create new Web Service
2. Connect repository
3. Set build command: `poetry install && alembic upgrade head`
4. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## 🧪 Testing

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=app --cov-report=html

# Run specific test file
poetry run pytest tests/test_auth.py
```

## 📝 Database Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

## 🔍 Code Quality

```bash
# Linting
poetry run ruff check .

# Formatting
poetry run ruff format .

# Type checking
poetry run mypy .
```

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [Pydantic v2 Documentation](https://docs.pydantic.dev/2.0/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Poetry Documentation](https://python-poetry.org/docs/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Join our community discussions

---

**Happy coding! 🚀**
