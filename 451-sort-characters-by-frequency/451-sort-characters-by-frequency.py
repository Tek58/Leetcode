class Solution:
    def frequencySort(self, s: str) -> str:
        store = Counter(s)
        heap = []
        for key, value in store.items():
            heapq.heappush(heap, (-value, key))
        
        res = ""
        while heap:
            val, letter = heapq.heappop(heap)
            curr = str(letter)*(-val)
            res += curr
        return res