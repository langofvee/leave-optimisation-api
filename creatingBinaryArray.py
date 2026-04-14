from datetime import datetime, date, timedelta

def create_binary_array(listOfLeaveDates: list[date]) -> list[int]:

    binaryArray = []

    startDate = listOfLeaveDates[0]
    endDate = listOfLeaveDates[-1]

    # marking leave days as 1 and letting non-leave days be zero
    # error -> i only works for int and not date, date is not a data type
    currentDate = startDate
    leave_set = set(listOfLeaveDates)  # set(non repetitive list) of all the leave dates

    while currentDate <= endDate:
        if currentDate in leave_set:
            binaryArray.append(1)
        elif currentDate.isoweekday() == 6 or currentDate.isoweekday() == 7:
            binaryArray.append(1)
        else:
            binaryArray.append(0)
        currentDate += datetime.timedelta(days=1)

    return binaryArray