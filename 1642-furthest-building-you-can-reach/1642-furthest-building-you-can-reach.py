class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        res = 0
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            heapq.heappush(heap, -diff)
            if diff > 0:
                bricks -= diff
            while bricks < 0 and ladders > 0:
                bricks += -heapq.heappop(heap)
                ladders -= 1
        
            if bricks < 0 and ladders == 0:
                break
            res = i
        
        return res     
