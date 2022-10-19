class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for i in words:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        heap = []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result