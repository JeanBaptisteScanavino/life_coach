from sqlalchemy import Column, Integer, String

from database.database import Base


class WaitingList(Base):
    __tablename__ = "waiting_list"

    id = Column(Integer, primary_key=True, index=True)
    category_id: Column(Integer)
    value = Column(String)
