from pydantic import BaseModel


class Month(BaseModel):
    year: int
    active: bool

    class Config:
        orm_mode = True