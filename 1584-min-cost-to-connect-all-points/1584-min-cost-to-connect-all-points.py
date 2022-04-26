import heapq as h
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        visited = set()
        for i in range(len(points)):
            mini = float('inf')
            for j in range(i+1,len(points)):
                x = abs(points[i][0]-points[j][0])
                y = abs(points[i][1]-points[j][1])
                h.heappush(heap,(x+y,i,j))

        length = len(points)
        leader = [i for i in range(length)]
        def find(node):
            if leader[node] == node:
                return node
            return find(leader[node])
        
        def Union(n1, n2):
            n1Leader = find(n1)
            n2Leader = find(n2)
            leader[n1Leader] = n2Leader
            
        cost = 0
        count = 0
        while heap:
            distance,n1,n2= h.heappop(heap)
            if count == length - 1:
                return cost
            n1Leader = find(n1)
            n2Leader = find(n2)
            if n1Leader != n2Leader:
                cost += distance
                count += 1
                visited.add((n1, n2))
                Union(n1, n2)
        return cost