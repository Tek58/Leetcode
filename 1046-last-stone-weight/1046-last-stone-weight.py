import heapq as heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap_list = []
        for i in stones:
            heap.heappush(heap_list,-i)
        
        while len(heap_list) > 1:
            x = -heap.heappop(heap_list)
            y = -heap.heappop(heap_list)
            
            if x != y :
                heap.heappush(heap_list, y-x)
        
        return 0 if not heap_list else -heap_list[0]
                