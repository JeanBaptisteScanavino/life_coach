from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.schemas.Month import MonthSchema
from core.use_case.month.create import CreateMonth
from core.use_case.month.get_all import GetAllMonth
from core.use_case.month.get_one import GetOnemonth
from database.models.Month import Month
from database.repository.month import MonthRepository
from database.database import get_db

month_router = APIRouter(
    prefix="/month",
    tags=["month"],
)

dependencies = {}
dependencies["month_repository"] = MonthRepository
dependencies["month_model"] = Month

@month_router.get("/")
def get_all_month(db: Session = Depends(get_db)):
    dependencies["db"] = db
    months = GetAllMonth(dependencies).get_all_month()
    return {"month": months}


@month_router.get("/{id}")
def get_one_month(id: int, db: Session = Depends(get_db)):
    dependencies["db"] = db
    month = GetOnemonth(dependencies).get_one_month(id)
    return {"month": month }


@month_router.post("/")
def create_month(db: Session = Depends(get_db)):
    dependencies["db"] = db
    month = CreateMonth(dependencies).create_month()
    return {"month": month}


# @month_router.put("/{id}")
# def update_month(id: int, month: Month):
#     return {"month": month}


# @month_router.get("/{id}/delete")
# def desactivate_month(id: int):
#     # month.active = false
#     return {"month": {"title": "My title", "active": False}}
