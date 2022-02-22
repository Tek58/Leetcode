class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incoming = [0]*numCourses
        neighbors = defaultdict(list)
        queue = deque()
        result = []
        
        for edge in prerequisites:
            neighbors[edge[1]].append(edge[0])
        
        for value in neighbors.values():
            for i in value:
                incoming[i] += 1
            
        for i in range(len(incoming)):
            if incoming[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for i in neighbors[curr]:
                incoming[i] -= 1
                if incoming[i] == 0:
                    queue.append(i)
                    
        if incoming.count(0) == numCourses:
            return result
        return []