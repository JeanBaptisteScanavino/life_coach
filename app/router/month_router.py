from fastapi import APIRouter

from core.schemas.Month import MonthSchema

month_router = APIRouter(
    prefix="/month",
    tags=["month"],
)


@month_router.get("/")
def get_all_month():
    return {"month": ["1", "2"]}


@month_router.get("/{id}")
def get_one_month(id: int):
    return {"month": id}


@month_router.post("/")
def create_month():
    # create use case New Month is Now or next
    jan = Month(year=2024, active=True)
    return {"month": jan}


# @month_router.put("/{id}")
# def update_month(id: int, month: Month):
#     return {"month": month}


# @month_router.get("/{id}/delete")
# def desactivate_month(id: int):
#     # month.active = false
#     return {"month": {"title": "My title", "active": False}}
