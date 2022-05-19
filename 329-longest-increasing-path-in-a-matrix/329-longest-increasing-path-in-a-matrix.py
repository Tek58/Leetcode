class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m , n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def isValid(newRow, newCol, row, col):
            return 0 <= newRow < m and 0 <= newCol < n and matrix[row][col] < matrix[newRow][newCol]
        
        @lru_cache(maxsize = None)
        def dfs(row, col):
            temp_res = 1
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                if isValid(newRow, newCol, row, col):
                    temp_res = max(temp_res, dfs(newRow, newCol) +1)
            return temp_res
        
        res = float("-inf")
        for row in range(m):
            for col in range(n):
                res = max(res, dfs(row, col))
        
        return res
                