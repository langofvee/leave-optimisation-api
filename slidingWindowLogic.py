from datetime import date, datetime

from pydantic import BaseModel
#from main import leavesInfo

class leavesInfo(BaseModel):
    numOfLeaves: int
    datesForLeaves: list[date]

class LeavesChunk(BaseModel):
    startDate: date
    endDate: date
    leaveDates: list[date]
    totalLeaves: int
    leavesUsed: int


    def slidingWindowLogic(self, windowLen: int,binaryArray:list[int]):
        leaveDates=[]
        global chunk
        chunk = LeavesChunk(
                    startDate=date.today(),
                    endDate=date.today(),
                    leaveDates=leaveDates,
                    totalLeaves=0,
                    leavesUsed=0
                )
        windowSum = 0

        for i in range (0,windowLen):
                windowSum = windowSum + int(binaryArray[i])

        f=0
        l=windowLen-1


        while l < len(binaryArray)-1:
            windowSum = windowSum - binaryArray[f]
            f+=1
            windowSum = windowSum + binaryArray[l]
            l=l+1

            if (l-f) >= len(binaryArray)-3:
                startDate = leavesInfo.datesForLeaves[0] + datetime.timedelta(days=f)
                endDate = leavesInfo.datesForLeaves[0] + datetime.timedelta(days=l)
                leaveDates=[]
                leavesUsed=0
                for i in range (startDate, endDate+1):
                    leaveDates.append(leavesInfo.datesForLeaves[0]+datetime.timedelta(days=i))
                    if binaryArray[i] == 0:
                        leavesUsed += 1

                totalLeaves = i-1

                chunk = LeavesChunk(
                    startDate=startDate,
                    endDate=endDate,
                    leaveDates=leaveDates,
                    totalLeaves=totalLeaves,
                    leavesUsed=leavesUsed
                )

        return(chunk)


    if __name__ == "__main__":
        binary = [1, 0, 0, 1, 0]
        slidingWindowLogic(windowLen=3, binaryArray=binary)