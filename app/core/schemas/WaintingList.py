from pydantic import BaseModel


class WaitingList(BaseModel):
    value: str
    category_id: int

    class Config:
        orm_mode = True