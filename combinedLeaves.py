#take leaves from calendarific API and user input, and return all the dates of leaves and holidays in a single list

from calendarific import calendarificCall
from models import (
    calendarificInput,
    combinedListOfLeaves,
    leavesInfo,
)


def combineLeavesAndHolidays(leavesInfo: leavesInfo, calendarificInput: calendarificInput) -> combinedListOfLeaves:
    
    listOfHolidays = calendarificCall(calendarificInput.country, calendarificInput.year, calendarificInput.type)
    
    listOfLeaves = leavesInfo.datesForLeaves
    
    combinedList = listOfHolidays + listOfLeaves
    
    return combinedList