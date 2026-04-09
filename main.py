import datetime

from django.db.models.functions import window
from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()


# numOfLeaves=Leaves that a user gets, non-Sunday, non-Saturday
# datesForLeaves=Date of each leave, non-Sunday, non-Saturday
# dates are in YYYY-MM-DD format
class leavesInfo(BaseModel):
    numOfLeaves: int
    datesForLeaves: list[date]

class leavesChunk(BaseModel):
    startDate: date
    endDate: date
    leaveDates: list[date]
    totalLeaves: int
    leavesUsed: int

class leavePlan(BaseModel):
    plan: list[leavesChunk]


########################
@app.get("/")
def home():
    return {"message": "So we're building a Leave Optimisation API"}

########################
@app.post("/optimising")
def accept_details(data: leavesInfo):
    if len(data.datesForLeaves) != data.numOfLeaves:
        raise HTTPException(status_code=400, detail="the number of leaves and number of dates entered do not match")


    # startYear = data.datesForLeaves[0].year
    # endYear = startYear + 1

    binaryArray = []

    startDate = data.datesForLeaves[0]
    endDate = data.datesForLeaves[-1]

    # marking leave days as 1 and letting non-leave days be zero
    # error -> i only works for int and not date, date is not a data type
    currentDate = startDate
    while currentDate <= endDate:
        leave_set = set(data.datesForLeaves)
        if currentDate in leave_set:
            binaryArray.append(1)
        elif currentDate.isoweekday() == 6 or currentDate.isoweekday() == 7:
            binaryArray.append(1)
        else:
            binaryArray.append(0)
        currentDate += datetime.timedelta(days=1)

    # TODO: sliding window approach to go through the binary array and
    # put down the holiday+leave days range
    windowLen=3
    while windowLen<=leavesInfo.numOfLeaves:
        sum=0
        for i in range (0,windowLen):
            sum=sum+int(binaryArray[i])

            f=int(binaryArray[0])
            l=int(binaryArray[windowLen-1])

            while l < windowLen:
                sum=sum-f
                f+=1
                sum=sum+l
                l=l+1

            if sum >= 3:
                leavesChunk.numOfLeaves=sum
                # TODO: update the startdate and enddate
                leavesChunk.startDate=currentDate
                leavesChunk.endDate=currentDate

    for i in range(0, len(binaryArray)):
        # we assume that 5 days is the maximum range that we can provide the user with
        if binaryArray[i] == 1:
            "sliding window approach to find the max ranges"
            "store the range + number of leave days it takes in a list of [date1,date2, no of leaves)"

    # TODO: run a sorting loop from max to min no of leaves occupied and display the date ranges
    # until the total sum is less than total number of leaves
