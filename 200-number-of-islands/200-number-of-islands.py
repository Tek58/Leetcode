class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] != "0":
                    visited.add((i, j))
                    count += 1
                    self.dfs(i, j, grid, visited, directions)
        return count
    
    def dfs(self, row, col, grid, visited, directions):
        for i in directions:
            newRow = row + i[0]
            newCol = col + i[1]
            curr = (newRow, newCol)
            if self.isValid(curr, grid, visited):
                visited.add(curr)
                self.dfs(newRow, newCol, grid, visited, directions)
                
                
    def isValid(self, curr, grid, visited):
        return curr not in visited and 0 <= curr[0] < len(grid) \
                and 0 <= curr[1] < len(grid[0]) and grid[curr[0]][curr[1]] != "0"
