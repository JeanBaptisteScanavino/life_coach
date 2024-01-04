from database.database import Base
from sqlalchemy import Column, Integer, String


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(String)
    month_id: Column(Integer)
    category_id: Column(Integer)
    active = Column(String, default="TODO")