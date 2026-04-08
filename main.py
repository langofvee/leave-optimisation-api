import datetime

from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()


# numOfLeaves=Leaves that a user gets, non-Sunday, non-Saturday
# datesForLeaves=Date of each leave, non-Sunday, non-Saturday
# dates are in YYYY-MM-DD format
class LeavesInfo(BaseModel):
    numOfLeaves: int
    datesForLeaves: list[datetime.date]


########################
''''@app.get("/")
def home():
    return {"message": "So we're building a Leave Optimisation API"}


@app.get("/leaves/{total_leaves}")
def get_leaves(leaves_given: int):
    return {"message": f"total number of leaves is {leaves_given}"}
'''


@app.post("/optimising")
def accept_details(data: LeavesInfo):
    if len(data.datesForLeaves) != data.numOfLeaves:
        raise HTTPException(status_code=400, detail="the number of leaves and number of dates entered do not match")

    else:
        startYear = data.datesForLeaves[0].year
        endYear = startYear + 1

        binaryArray = []

        # the starting date won't necessarily be 01.01.xxxx
        # we need to run a loop from start date to end date
        startDate = data.datesForLeaves[0]
        endDate = data.datesForLeaves[-1]

        c = 0  # counter
        # marking leave days as 1 and letting non-leave days be zero
        # error -> i only works for int and not date, date is not a data type
        currentDate = startDate
        while startDate <= endDate:
            if currentDate in data.datesForLeaves:
                binaryArray.append(1)
            elif date.isoweekday(currentDate) is 6 or date.isoweekday(currentDate) is 7:
                binaryArray.append(1)
            else:
                binaryArray.append(0)
            c += 1

        """sliding window approach to go through the binary array and
        put down the holiday+leave days range"""
        for i in range(0, 365):
            # we assume that 5 days is the maximum range that we can provide the user with
            if binaryArray[i] == 1:
                "sliding window approach to find the max ranges"
                "store the range + number of leave days it takes in a list of [date1,date2, no of leaves)"

        "we run a sorting loop from max to min no of leaves occupied and display the date ranges "
        "until the total sum is less than total number of leaves"
