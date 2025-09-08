
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Environment
    ENV: str = "local"

    # Database
    DATABASE_URL: str = "sqlite:///./dev.db"

    # JWT
    JWT_SECRET: str = "change-me"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # External Services
    STRIPE_SECRET_KEY: str | None = None
    STRIPE_PUBLISHABLE_KEY: str | None = None

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Py API Starter"

    # Background Jobs
    USE_CELERY: bool = False  # Set to True to use Celery instead of APScheduler

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
