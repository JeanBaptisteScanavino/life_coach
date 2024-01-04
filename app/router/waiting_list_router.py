from core.schemas.WaintingList import WaitingList
from fastapi import APIRouter

waiting_list_router = APIRouter(
    prefix="/waiting_list",
    tags=["waiting_list"],
)


@waiting_list_router.get("/")
def get_all_waiting_list():
    return {"waiting_list": {"cat 1": ["1", "2"], "cat 2": ["voila", "aitre"]}}


# @waiting_list_router.get("/{id}")
# def get_one_waiting_list(id: int):
#     return {"waiting_list": id}


@waiting_list_router.post("/")
def create_waiting_list(value: str, category_id: int):
    # create use case New wainting list
    new_wait = WaitingList(value=value, category_id=category_id)
    return {"waiting_list": new_wait}


# @waiting_list_router.put("/{id}")
# def update_waiting_list(id: int, waiting_list: Month):
#     return {"waiting_list": waiting_list}


@waiting_list_router.get("/{id}/delete")
def desactivate_waiting_list(id: int):
    # waiting_list.active = false
    return {"waiting_list": "is deleted"}
