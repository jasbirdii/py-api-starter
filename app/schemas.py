from datetime import UTC, datetime

from pydantic import BaseModel, EmailStr

from .models import ItemStatus, UserRole


# User schemas
class UserBase(BaseModel):
    """Base user schema."""
    email: EmailStr
    username: str
    full_name: str | None = None
    is_active: bool = True
    role: UserRole = UserRole.USER


class UserCreate(UserBase):
    """User creation schema."""
    password: str


class UserUpdate(BaseModel):
    """User update schema."""
    email: EmailStr | None = None
    username: str | None = None
    full_name: str | None = None
    is_active: bool | None = None
    role: UserRole | None = None


class UserInDB(UserBase):
    """User in database schema."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class User(UserInDB):
    """User response schema."""
    pass


# Item schemas
class ItemBase(BaseModel):
    """Base item schema."""
    title: str
    description: str | None = None
    status: ItemStatus = ItemStatus.ACTIVE
    price: float | None = None


class ItemCreate(ItemBase):
    """Item creation schema."""
    pass


class ItemUpdate(BaseModel):
    """Item update schema."""
    title: str | None = None
    description: str | None = None
    status: ItemStatus | None = None
    price: float | None = None


class ItemInDB(ItemBase):
    """Item in database schema."""
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class Item(ItemInDB):
    """Item response schema."""
    owner: User


class ItemWithOwner(ItemInDB):
    """Item with owner details."""
    owner: User


# Payment schemas
class PaymentBase(BaseModel):
    """Base payment schema."""
    amount: float
    currency: str = "usd"


class PaymentCreate(PaymentBase):
    """Payment creation schema."""
    item_id: int | None = None


class PaymentInDB(PaymentBase):
    """Payment in database schema."""
    id: int
    status: str
    stripe_payment_intent_id: str | None = None
    user_id: int
    item_id: int | None = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class Payment(PaymentInDB):
    """Payment response schema."""
    pass


# Auth schemas
class Token(BaseModel):
    """Token response schema."""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token data schema."""
    username: str | None = None


# Health check schema
class HealthResponse(BaseModel):
    """Health check response schema."""
    status: str
    env: str
    timestamp: datetime = datetime.now(UTC)
