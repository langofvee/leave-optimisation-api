import datetime
from datetime import date

from pydantic import BaseModel

# numOfLeaves=Leaves that a user gets, non-Sunday, non-Saturday
# datesForLeaves=Date of each leave, non-Sunday, non-Saturday
# dates are in YYYY-MM-DD format


#input schemas for the API
class calendarificInput(BaseModel):
    country: str = "IN"
    years: list[int] = [datetime.datetime.now(tz=datetime.timezone.utc).year]
    type: str = "national"  # national, religious, local, observance
    # month: int = datetime.datetime.now(tz=datetime.timezone.utc).month
    
    
class leavesInfo(BaseModel):
    numOfLeaves: int
    datesForLeaves: list[date]
    
    saturdayIncluded: bool = True
    sundayIncluded: bool = True
    mondayIncluded: bool = False
    tuesdayIncluded: bool = False
    wednesdayIncluded: bool = False
    thursdayIncluded: bool = False
    fridayIncluded: bool = False
    
    sandwichLeavesConsidered: bool = False #sandwich leaves to be considered later in the algorithm
    
    calendarificData: calendarificInput = calendarificInput()
  
  
  
  
#schemas for algorithm processing  
class combinedListOfLeaves(BaseModel):
    leaveDates: list[date]
    holidayDates: list[date]



  
    
#sub-output model for the API  

# class CalendarificOutput(BaseModel):
#     pass

class leavesChunk(BaseModel):
    startDate: date
    endDate: date
    leaveDates: list[date]
    totalLeaves: int
    leavesUsed: int

#output model for the API
class leavePlan(BaseModel):
    plan: list[leavesChunk]