#gives the list of holidays from Calendarific API for a given country, years and type of holiday

"""Calendarific standard API response:
{
    "meta": {
        "code": 200
    },
    "response": {
        "holidays": [
            {
                "name": "Name of holiday goes here",
                "description": "Description of holiday goes here",
                "date": {
                    "iso": "2018-12-31",
                    "datetime": {
                        "year": 2018,
                        "month": 12,
                        "day": 31
                    }
                },
                "type": [
                    "Type of Observance goes here"
                ]
            }
        ]
    }
}"""


import os
from datetime import date

import httpx
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("CALENDARIFIC_API_KEY")


def calendarificCall( country: str, years: list[int], type: str) -> list[date]:
    
    holidaysSchema= []
    
    for year in years:
        responses = httpx.get(
            "https://calendarific.com/api/v2/holidays",
            params={
                "api_key": api_key,
                "country": country,
                "year": year,
                "type": type,
            },
        )
        holidaysSchema.append(responses.json()["response"]["holidays"])
    
    listOfAllHolidays = []
    
    for holidaysPerYear in holidaysSchema:
        for holiday in holidaysPerYear:
            listOfAllHolidays.append(holiday["date"]["iso"])

    return listOfAllHolidays