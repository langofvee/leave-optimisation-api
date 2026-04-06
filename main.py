from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()


class UserInfo(BaseModel):
    name: str
    total_leaves: int
    dates: list[date]


########################
@app.get("/")
def home():
    return {"message": "So we're building a Leave Optimisation API"}


@app.get("/leaves/{total_leaves}")
def get_leaves(total_leaves: int):
    return {"message": f"total number of leaves is {total_leaves}"}


@app.post("/leaves")
def accept_details(data : UserInfo):
    if len(data.dates)!=data.total_leaves:
        raise HTTPException(status_code=400, detail="the number of leaves and dates do not match")
    return {"message": f"the name entered is {data.name} and the number of leaves is {data.total_leaves}"}
