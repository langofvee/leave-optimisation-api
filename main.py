from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

from schemas import calendarificInput, leavePlan, leavesInfo
from slidingWindowLogic import slidingWindowLogic

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
        # sliding window logic to find the best chunk of leaves
        slidingWindowOutput = slidingWindowLogic(dataInputLeaves, dataCalendarific)
        print(slidingWindowOutput)
