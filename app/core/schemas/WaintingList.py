from pydantic import BaseModel


class WaitingListSchema(BaseModel):
    value: str
    category_id: int

    class Config:
        orm_mode = True
