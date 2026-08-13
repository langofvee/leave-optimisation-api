import datetime
import os
from datetime import date

# from django.db.models.functions import window
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

import creatingBinaryArray
from models import calendarificInput, leavePlan, leavesChunk, leavesInfo

load_dotenv()

app = FastAPI()

########################
@app.get("/")
def home():
    return {"message": "So we're building a Leave Optimisation API"}


########################

@app.post("/optimiseLeaves", response_model=leavePlan)

def accept_details(data: leavesInfo):
    if len(data.datesForLeaves) != data.numOfLeaves:
        raise HTTPException(
            status_code=400,
            detail="the number of leaves and number of dates entered do not match",
        )

    startDate = data.datesForLeaves[0]
    endDate = data.datesForLeaves[-1]

    binaryArray = creatingBinaryArray(data.datesForLeaves)
    leaveChunkList = []

    # TODO: sliding window approach to go through the binary array and
    # put down the holiday+leave days range
    windowLen = 3
    while windowLen <= data.numOfLeaves:
        sum = 0
        for i in range(windowLen):
            sum = sum + int(binaryArray[i])

            f = int(binaryArray[0])
            l = int(binaryArray[windowLen - 1])

            while l < windowLen:
                sum = sum - f
                f += 1
                sum = sum + l
                l = l + 1

            if sum >= 3:
                leaveChunkList.append(
                    leavesChunk(
                        startDate=data.datesForLeaves[0]
                        + datetime.timedelta(days=f),
                        endDate=data.datesForLeaves[0]
                        + datetime.timedelta(days=l),
                        # leaveDates=
                    )
                )

    for i in range(0, len(binaryArray)):
        # we assume that 5 days is the maximum range that we can provide the user with
        if binaryArray[i] == 1:
            "sliding window approach to find the max ranges"
            "store the range + number of leave days it takes in a list of [date1,date2, no of leaves]"

    # TODO: run a sorting loop from max to min no of leaves occupied and display the date ranges
    # until the total sum is less than total number of leaves
