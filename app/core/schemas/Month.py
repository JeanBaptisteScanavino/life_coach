from pydantic import BaseModel
from enum import Enum

class MonthEnum(Enum):
    JAN : "January"
    FEB : "February"
    MAR : "March"
    APR : "April"
    MAY : "May"
    JUN : "June"
    JUL : "July"
    AUG : "August"
    SEP : "September"
    OCT : "October"
    NOV : "November"
    DEC : "December"

class MonthSchema(BaseModel):
    year: int
    name: MonthEnum
    active: bool
