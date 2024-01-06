from sqlalchemy import Column, Integer, String, ForeignKey

from database.database import Base


class WaitingList(Base):
    __tablename__ = "waiting_list"

    id: int = Column(Integer, primary_key=True, index=True)
    category_id: int = Column(Integer)
    value: str = Column(String)
