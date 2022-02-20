class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap, i)
            else:
                top = heapq.heappop(heap)
                heapq,heappush(heap, max(top, i))
        return heapq.heappop(heap)