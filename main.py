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

def accept_details(dataInputLeaves: leavesInfo, dataCalendarific: calendarificInput):
    if len(dataInputLeaves.datesForLeaves) != (dataInputLeaves.numOfLeaves):
        raise HTTPException(
            status_code=400,
            detail="the number of leaves and number of dates entered do not match",
        )
    else:
        #sliding window logic to find the best chunk of leaves

