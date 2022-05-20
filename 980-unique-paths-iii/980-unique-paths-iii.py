class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        uniquePaths, empty = 0, 1
        
        def dfs(row, col, empty):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 0

            if grid[row][col] == -1:
                return 0

            if grid[row][col] == 2:
                if empty == 0:
                    return 1
                return 0

            grid[row][col] = -1
            count = dfs(row-1, col, empty-1) + dfs(row+1, col, empty-1) + dfs(row, col+1, empty-1) + dfs(row, col-1, empty-1)
            grid[row][col] = 0

            return count
    
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    x, y = row, col
                elif grid[row][col] == 0:
                    empty += 1
        
        uniquePaths = dfs(x, y, empty)
        return uniquePaths
    
    