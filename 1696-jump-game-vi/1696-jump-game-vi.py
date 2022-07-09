class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = []
        res = 0
        for i in range(len(nums)):
            maxVal = 0
            if heap:
                maxVal, idx = heap[0]
                while idx + k < i:
                    maxVal, idx = heapq.heappop(heap)
                heapq.heappush(heap, [maxVal, idx])
            res = nums[i] + -maxVal
            heapq.heappush(heap, [-res, i]) 
        return res
