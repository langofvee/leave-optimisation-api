from datetime import date, datetime, timedelta

from main import leavesInfo


def create_binary_array(listOfLeaveDates: leavesInfo.datesForLeaves) -> list[int]:

    binaryArray = []

    startDate = listOfLeaveDates[0]
    endDate = listOfLeaveDates[-1]

    # marking leave days as 1 and letting non-leave days be zero
    # error -> i only works for int and not date, date is not a data type
    currentDate = startDate
    leave_set = set(listOfLeaveDates)  # set(non repetitive list) of all the leave dates

    while currentDate <= endDate:
        if currentDate in leave_set or (currentDate.isoweekday() == 6 and leavesInfo.saturdayIncluded) or (currentDate.isoweekday() == 7 and leavesInfo.sundayIncluded):
            binaryArray.append(1)
        else:
            binaryArray.append(0)
        currentDate += datetime.timedelta(days=1)

    return binaryArray
