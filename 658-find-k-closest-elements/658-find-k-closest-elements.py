import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        container = []
        for i in arr:
            val = abs(i-x)
            heapq.heappush(container, (val,i))
            
        result = []
        for i in range(k):
            res = heapq.heappop(container)[1] 
            result.append(res)
        result.sort()
        return result