from datetime import timedelta

from schemas.models import calendarificInput, leavesInfo
from services.combinedLeaves import combineLeavesAndHolidays

# input from combinedLeaves.py


def createBinaryArray(
    listOfLeaveDates: leavesInfo.datesForLeaves, calendarificInput: calendarificInput
) -> list[int]:
    binaryArray = []
    combinedList = combineLeavesAndHolidays(leavesInfo, calendarificInput)
    combinedList.sort()

    startDate = combinedList[0]
    endDate = combinedList[-1]

    for i in range(startDate, endDate + timedelta(days=1), timedelta(days=1)):
        if i in combinedList:
            binaryArray.append(1)
        else:
            binaryArray.append(0)

    return binaryArray
