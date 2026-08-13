import json
import os

import httpx
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()

api_key = os.getenv("CALENDARIFIC_API_KEY")

response = httpx.get(
    "https://calendarific.com/api/v2/holidays",
    params={
        "api_key": api_key,
        "country": "IN",
        "year": 2026,
        "type": "national",
        "month": 8,
    },
)
data = response.json()

print(response.status_code)
print(json.dumps(data, indent=4, sort_keys=True))
