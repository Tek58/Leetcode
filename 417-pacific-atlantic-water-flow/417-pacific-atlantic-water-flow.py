class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(r, c, visited, prevHeight):
            if (r, c) not in visited and 0 <= r < ROWS and 0 <= c < COLS and prevHeight <= heights[r][c]:
                visited.add((r, c))
                dfs(r + 1, c, visited, heights[r][c])
                dfs(r - 1, c, visited, heights[r][c])
                dfs(r, c + 1, visited, heights[r][c])
                dfs(r, c - 1, visited, heights[r][c])
                
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        # print(pacific,atlantic)
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res
            