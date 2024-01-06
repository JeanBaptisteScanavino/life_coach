from enum import Enum

from pydantic import BaseModel


class SkillStatus(Enum):
    TODO: "todo"
    STARTED: "started"
    FINISHED: "finished"


class SkillSchema(BaseModel):
    value: str
    category_id: int
    month_id: int
    status: str
