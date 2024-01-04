from pydantic import BaseModel


class Month(BaseModel):
    year: int
    active: bool
