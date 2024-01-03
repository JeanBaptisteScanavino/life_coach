from fastapi import APIRouter

from core.models.Category import Category

category_router = APIRouter(
    prefix="/category",
    tags=["category"],
)


@category_router.get("/")
def get_all_category():
    return {"category": ["1", "2"]}


@category_router.get("/{id}")
def get_one_category(id: int):
    return {"category": id}


@category_router.post("/")
def create_category(category: Category):
    return {"category": category}


@category_router.put("/{id}")
def update_category(id: int, category: Category):
    return {"category": category}


@category_router.get("/{id}/delete")
def desactivate_category(id: int):
    # category.active = false
    return {"category": {"title": "My title", "active": False}}
