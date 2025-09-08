from datetime import UTC, datetime
from enum import Enum

from sqlmodel import Field, Relationship, SQLModel


class UserRole(str, Enum):
    """User roles."""
    ADMIN = "admin"
    USER = "user"


class ItemStatus(str, Enum):
    """Item status."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"


class User(SQLModel, table=True):
    """User model."""
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    username: str = Field(unique=True, index=True)
    hashed_password: str
    full_name: str | None = None
    is_active: bool = Field(default=True)
    role: UserRole = Field(default=UserRole.USER)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # Relationships
    items: list["Item"] = Relationship(back_populates="owner")


class Item(SQLModel, table=True):
    """Item model."""
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str | None = None
    status: ItemStatus = Field(default=ItemStatus.ACTIVE)
    price: float | None = None
    owner_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # Relationships
    owner: User = Relationship(back_populates="items")


class Payment(SQLModel, table=True):
    """Payment model."""
    id: int | None = Field(default=None, primary_key=True)
    amount: float
    currency: str = Field(default="usd")
    status: str  # pending, succeeded, failed, canceled
    stripe_payment_intent_id: str | None = None
    user_id: int = Field(foreign_key="user.id")
    item_id: int | None = Field(foreign_key="item.id", default=None)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
