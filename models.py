from pydantic import BaseModel
from datetime import date
import datetime

# numOfLeaves=Leaves that a user gets, non-Sunday, non-Saturday
# datesForLeaves=Date of each leave, non-Sunday, non-Saturday
# dates are in YYYY-MM-DD format
# 
class calendarificInput(BaseModel):
    country: str = "IN"
    year: int = datetime.datetime.now(tz=datetime.timezone.utc).year
    type: str = "national"  # national, religious, local, observance
    month: int = datetime.datetime.now(tz=datetime.timezone.utc).month
    
class leavesInfo(BaseModel):
    numOfLeaves: int
    datesForLeaves: list[date]
    saturdayIncluded: bool = True
    sundayIncluded: bool = True
    sandwichLeavesConsidered: bool = True
    calendarificInput: calendarificInput = calendarificInput()
    


class leavesChunk(BaseModel):
    startDate: date
    endDate: date
    leaveDates: list[date]
    totalLeaves: int
    leavesUsed: int


class leavePlan(BaseModel):
    plan: list[leavesChunk]