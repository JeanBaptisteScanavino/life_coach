from core.schemas.Category import Category
from database.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

category_router = APIRouter(
    prefix="/category",
    tags=["category"],
)


@category_router.get("/")
def get_all_category(db: Session = Depends(get_db)):
    return {"category": ["1", "2"]}


@category_router.get("/{id}")
def get_one_category(id: int, db: Session = Depends(get_db)):
    return {"category": id}


@category_router.post("/")
def create_category(category: Category, db: Session = Depends(get_db)):
    cat = Category(title=category.title, active=True)
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return {"category": cat}


@category_router.put("/{id}")
def update_category(id: int, category: Category, db: Session = Depends(get_db)):
    return {"category": category}


@category_router.get("/{id}/delete")
def desactivate_category(id: int, db: Session = Depends(get_db)):
    # category.active = false
    return {"category": {"title": "My title", "active": False}}
