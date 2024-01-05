from pydantic import BaseModel


class MonthSchema(BaseModel):
    year: int
    active: bool

    class Config:
        orm_mode = True
