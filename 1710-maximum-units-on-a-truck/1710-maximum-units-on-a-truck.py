class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x:x[1], reverse=True)
        # print(boxTypes)
        count = 0
        for i, j in boxTypes:
            i = min(i, truckSize)
            count += i * j
            truckSize -= i
            if truckSize == 0:
                break
        return count
            