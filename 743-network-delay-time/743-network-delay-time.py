class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = DefaultDict(list)
        for edge in times:
            graph[edge[0]].append((edge[2], edge[1]))
        
        heap = [(0,k)]
        visited = [-1] * (n + 1)
        while heap:
            cost, node = heapq.heappop(heap)
            if visited[node] != -1:
                continue
            visited[node] = cost
            for child in graph[node]:
                heapq.heappush(heap, (cost + child[0], child[1]))
        
        if min(visited[1:]) == -1:
            return -1
        return max(visited)            