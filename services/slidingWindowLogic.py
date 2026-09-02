from schemas.models import calendarificInput, leavesChunk, leavesInfo
from services.creatingBinaryArray import createBinaryArray


# input from binary array
def slidingWindowLogic(
    leavesUser: leavesInfo, leavesCalendarific: calendarificInput
) -> list[leavesChunk]:

    # Create a binary array representing the leave and holiday dates
    binaryArray = createBinaryArray(leavesUser.datesForLeaves, leavesCalendarific)

    # Initialize variables for the sliding window
    maxLeavesUsed = 0
    bestChunks = []

    # Sliding window logic to find the best chunk of leaves
    for i in range(len(binaryArray)):
        for j in range(i, len(binaryArray)):
            currentChunk = binaryArray[i : j + 1]
            leavesUsed = sum(currentChunk)

            if leavesUsed > maxLeavesUsed:
                maxLeavesUsed = leavesUsed
                bestChunks = [
                    leavesChunk(
                        startDate=leavesUser.datesForLeaves[i],
                        endDate=leavesUser.datesForLeaves[j],
                        leaveDates=leavesUser.datesForLeaves[i : j + 1],
                        totalLeaves=len(currentChunk),
                        leavesUsed=leavesUsed,
                    )
                ]
            elif leavesUsed == maxLeavesUsed:
                bestChunks.append(
                    leavesChunk(
                        startDate=leavesUser.datesForLeaves[i],
                        endDate=leavesUser.datesForLeaves[j],
                        leaveDates=leavesUser.datesForLeaves[i : j + 1],
                        totalLeaves=len(currentChunk),
                        leavesUsed=leavesUsed,
                    )
                )

    return bestChunks
