class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap, int(i))
            else:
                top = heapq.heappop(heap)
                heapq,heappush(heap, max(top, int(i)))
        return str(heapq.heappop(heap))