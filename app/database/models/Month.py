from sqlalchemy import Boolean, Column, Integer, String

from database.database import Base


class Month(Base):
    __tablename__ = "months"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    year = Column(Integer, index=True)
    active = Column(Boolean, default=True)
