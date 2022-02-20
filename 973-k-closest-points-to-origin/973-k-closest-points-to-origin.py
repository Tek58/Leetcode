class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for j in range(len(points)):
            distance = math.sqrt((points[j][1])**2 + (points[j][0])**2)
            index_val = [distance, j]
            heapq.heappush(heap, (-distance, points[j]))
            if len(heap) > K:
                heapq.heappop(heap)
        
        result = []
        while heap:
            curr = heapq.heappop(heap)
            result.append(curr[1])
        return result