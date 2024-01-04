from database.database import Base
from sqlalchemy import Boolean, Column, Integer, String


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    active = Column(Boolean, default=True)
