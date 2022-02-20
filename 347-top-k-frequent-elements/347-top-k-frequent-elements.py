class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = Counter(nums)
        heap = []
        for key, value in store.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            top = heapq.heappop(heap)
            result.append(top[1])
        return result
                