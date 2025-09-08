from sqlmodel import Session, SQLModel, create_engine

from .config import settings

# Create engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.ENV == "local",  # Log SQL queries in local environment
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)


def create_db_and_tables():
    """Create database tables."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency to get database session."""
    with Session(engine) as session:
        yield session
