class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        heap = [(0, 0, 0)]
        # minEffort = float("inf")
        
        def isValid(row, col):
            return (row, col) not in visited and 0 <= row < n \
                    and 0 <= col < m
        
        while heap:
            maxDifference, row, col = heapq.heappop(heap)
            
            # minEffort = min(minEffort, maxDifference)
            if (row, col) == (n-1, m-1):
                return maxDifference
            
            if (row, col) in visited:
                continue
                
            visited.add((row, col))
            
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                if isValid(newRow, newCol):
                    operation = abs(heights[row][col] - heights[newRow][newCol])
                    newDifference = max(maxDifference, operation)
                    heapq.heappush(heap, (newDifference, newRow, newCol))
        
        return maxDifference
        