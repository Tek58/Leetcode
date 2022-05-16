class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0:
            return -1
            
        res = float("inf")
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        visited = set([(0,0)])
        queue = deque([(0, 0, 1)])
        
        def isValid(row, col):
            return 0 <= row < n and 0 <= col < n and (row, col) not in visited and grid[row][col] == 0
        
        while queue:
            x, y, level = queue.popleft()
            if (x, y) == (n-1, n-1):
                res = min(res, level)
            else:
                for direction in directions:
                    newX = x + direction[0]
                    newY = y + direction[1]
                    if isValid(newX, newY):
                        visited.add((newX, newY))
                        queue.append((newX, newY, level+1))
        return -1 if res == float("inf") else res
            