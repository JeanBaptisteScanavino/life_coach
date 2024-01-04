from database.database import Base
from sqlalchemy import Boolean, Column, Integer


class Month(Base):
    __tablename__ = "months"

    id = Column(Integer, primary_key=True, index=True)
    year: Column(Integer, index=True)
    active = Column(Boolean, default=True)
