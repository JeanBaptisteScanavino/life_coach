from fastapi import APIRouter

from .category_router import category_router

main_router = APIRouter()

main_router.include_router(category_router)
