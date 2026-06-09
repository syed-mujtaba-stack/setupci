from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Item])
def read_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve items.
    """
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items

@router.post("/", response_model=schemas.Item)
def create_item(*, db: Session = Depends(get_db), item_in: schemas.ItemCreate) -> Any:
    """
    Create new item.
    """
    item = models.Item(
        title=item_in.title,
        description=item_in.description,
        is_done=item_in.is_done
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/{id}", response_model=schemas.Item)
def read_item(*, db: Session = Depends(get_db), id: int) -> Any:
    """
    Get item by ID.
    """
    item = db.query(models.Item).filter(models.Item.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{id}", response_model=schemas.Item)
def update_item(*, db: Session = Depends(get_db), id: int, item_in: schemas.ItemUpdate) -> Any:
    """
    Update an item.
    """
    item = db.query(models.Item).filter(models.Item.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    update_data = item_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(item, field, value)
        
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{id}", response_model=schemas.Item)
def delete_item(*, db: Session = Depends(get_db), id: int) -> Any:
    """
    Delete an item.
    """
    item = db.query(models.Item).filter(models.Item.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return item
