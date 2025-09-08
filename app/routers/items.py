from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from ..db import get_session
from ..dependencies import get_current_user
from ..models import Item, User
from ..schemas import Item as ItemSchema
from ..schemas import ItemCreate, ItemUpdate, ItemWithOwner

router = APIRouter()


@router.post("/", response_model=ItemSchema)
def create_item(
    *,
    session: Session = Depends(get_session),
    item_data: ItemCreate,
    current_user: User = Depends(get_current_user)
) -> Any:
    """Create a new item."""
    db_item = Item(
        **item_data.model_dump(),
        owner_id=current_user.id
    )
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.get("/", response_model=list[ItemWithOwner])
def read_items(
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user)
) -> Any:
    """Retrieve items."""
    statement = select(Item).offset(skip).limit(limit)
    items = session.exec(statement).all()
    return items


@router.get("/{item_id}", response_model=ItemWithOwner)
def read_item(
    *,
    session: Session = Depends(get_session),
    item_id: int,
    current_user: User = Depends(get_current_user)
) -> Any:
    """Get item by ID."""
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Check if user owns the item or is admin
    if item.owner_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")

    return item


@router.put("/{item_id}", response_model=ItemSchema)
def update_item(
    *,
    session: Session = Depends(get_session),
    item_id: int,
    item_data: ItemUpdate,
    current_user: User = Depends(get_current_user)
) -> Any:
    """Update an item."""
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Check if user owns the item or is admin
    if item.owner_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")

    item_dict = item_data.model_dump(exclude_unset=True)
    for field, value in item_dict.items():
        setattr(item, field, value)

    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.delete("/{item_id}")
def delete_item(
    *,
    session: Session = Depends(get_session),
    item_id: int,
    current_user: User = Depends(get_current_user)
) -> Any:
    """Delete an item."""
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Check if user owns the item or is admin
    if item.owner_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")

    session.delete(item)
    session.commit()
    return {"message": "Item deleted successfully"}
