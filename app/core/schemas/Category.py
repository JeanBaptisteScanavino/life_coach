from pydantic import BaseModel


class Category(BaseModel):
    title: str
    active: bool
    
    class Config:
        orm_mode = True
