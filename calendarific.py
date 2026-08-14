#gives the list of holidays from Calendarific API for a given country, year and type of holiday

import os

import httpx
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("CALENDARIFIC_API_KEY")


def calendarificCall( country: str, year: int, type: str):
    
    response = httpx.get(
    "https://calendarific.com/api/v2/holidays",
    params={
        "api_key": api_key,
        "country": country,
        "year": year,
        "type": type,
    },
    )
    
    data = response.json()
    
    #gives all the holidays in the given year for the given country and type of holiday
    
    listOfHolidays = []

    holidays = data["response"]["holidays"]
    
    for holiday in holidays:
        listOfHolidays.append(holiday["date"]["iso"])

    return listOfHolidays