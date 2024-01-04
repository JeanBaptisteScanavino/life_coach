from fastapi import APIRouter

from .category_router import category_router
from .month_router import month_router
from .skill_router import skill_router
from .waiting_list_router import waiting_list_router

main_router = APIRouter()

router_list = [category_router, month_router, skill_router, waiting_list_router]
for router in router_list:
    main_router.include_router(router)
