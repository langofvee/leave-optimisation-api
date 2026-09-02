#take leaves from calendarific API and user input, and return all the dates of leaves and holidays in a single list

from schemas.models import (
    combinedListOfLeaves,
    leavesInfo,
)
from services.calendarific import calendarificCall


def combineLeavesAndHolidays(leavesInfo: leavesInfo) -> combinedListOfLeaves:
    
    """right now, the function takes "year" from leavesInfo.calendarificInput.year as input and considers all the holidays in that year. But if the leaves are in a different year, then it will not consider the holidays in that year. So we need to modify this function to take the year from the leavesInfo.datesForLeaves and consider all the holidays in that year as well. this can be done by taking the minimum and maximum dates from the leavesInfo.datesForLeaves and then calling the calendarificCall function from date start to date end in that range. Then we can combine all the holidays in a single list and return it along with the leavesInfo.datesForLeaves. This will ensure that we consider all the holidays in the range of years in which the leaves are taken."""
    
    def getYearsFromLeaveDates(datesForLeaves: list) -> list[int]:
        years = set()
        for date in datesForLeaves:
            years.add(date.year)
        return list(years)
        
    years = getYearsFromLeaveDates(leavesInfo.datesForLeaves)
    
    listOfHolidays = calendarificCall(country=leavesInfo.calendarificInput.country, years=years, type=leavesInfo.calendarificInput.type)
    
    listOfLeaves = leavesInfo.datesForLeaves
    
    combinedList = listOfHolidays + listOfLeaves
    
    return combinedList