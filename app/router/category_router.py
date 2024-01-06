from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.schemas.Category import CategorySchema
from core.use_case.category.create import CreateCategory
from core.use_case.category.delete import DeactivateCategory
from core.use_case.category.get_all import GetAllCategory
from core.use_case.category.get_one import GetOneCategory
from core.use_case.category.update import UpdateCategory
from database.database import get_db
from database.models.Category import Category
from database.repository.category import CategoryRepository

category_router = APIRouter(
    prefix="/category",
    tags=["category"],
)

dependencies = {}
dependencies["category_repository"] = CategoryRepository
dependencies["category_model"] = Category


@category_router.get("/")
def get_all_category(db: Session = Depends(get_db)):
    dependencies["db"] = db
    category = GetAllCategory(dependencies).execute()
    return {"category": category}


@category_router.get("/{id}")
def get_one_category(id: int, db: Session = Depends(get_db)):
    dependencies["db"] = db
    cat = GetOneCategory(dependencies).execute(id)
    return {"category": cat}


@category_router.post("/")
def create_category(category: CategorySchema, db: Session = Depends(get_db)):
    dependencies["db"] = db
    cat = CreateCategory(dependencies).execute(category)
    return {"category": cat}


@category_router.put("/{id}")
def update_category(id: int, category: CategorySchema, db: Session = Depends(get_db)):
    dependencies["db"] = db
    category = UpdateCategory(dependencies).execute(id, category)
    return {"category": category}


@category_router.get("/{id}/delete")
def desactivate_category(id: int, db: Session = Depends(get_db)):
    dependencies["db"] = db
    category = DeactivateCategory(dependencies).execute(id)
    return {"category": category}
