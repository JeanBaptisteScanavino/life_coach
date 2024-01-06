from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.use_case.waiting_list.delete import DeleteWaitingList
from core.use_case.waiting_list.create import CreateWaitingList
from core.use_case.waiting_list.get_all import GetAllWaitingList
from database.repository.waiting_list import WaitingListRepository

from core.schemas.WaintingList import WaitingListSchema
from database.models.WaintingList import WaitingList
from database.database import get_db

waiting_list_router = APIRouter(
    prefix="/waiting_list",
    tags=["waiting_list"],
)

dependencies = {}
dependencies["waiting_list_repository"] = WaitingListRepository
dependencies["waiting_list_model"] = WaitingList

@waiting_list_router.get("/")
def get_all_waiting_list(db: Session = Depends(get_db)):
    dependencies["db"] = db
    waiting_lists = GetAllWaitingList(dependencies).execute()
    return {"waiting_list": waiting_lists }


# @waiting_list_router.get("/{id}")
# def get_one_waiting_list(id: int):
#     return {"waiting_list": id}


@waiting_list_router.post("/")
def create_waiting_list(waiting_list: WaitingListSchema, db: Session = Depends(get_db)):
    # create use case New wainting list
    dependencies["db"] = db
    waiting_list = CreateWaitingList(dependencies).execute(waiting_list)
    return {"waiting_list": waiting_list}


# @waiting_list_router.put("/{id}")
# def update_waiting_list(id: int, waiting_list: Month):
#     return {"waiting_list": waiting_list}


@waiting_list_router.get("/{id}/delete")
def delete_waiting_list(id: int, db: Session = Depends(get_db)):
    dependencies["db"] = db
    try:
        DeleteWaitingList(dependencies).execute(id)
        return {"waiting_list": "IS_DELETED"}
    except Exception:
        return Exception