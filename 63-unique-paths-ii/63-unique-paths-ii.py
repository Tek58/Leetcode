class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        res = []
        m , n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 1 and 1 in obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        elif n == 1:
            for i in range(m):
                if obstacleGrid[i][0] == 1:
                    return 0
            
        for i in range(1):
            prev = False
            for j in range(n):
                if not prev:
                    val = 0 if obstacleGrid[i][j] else 1
                    res .append(val)
                    if not val:
                        prev = True
                else:
                    res.append(0)
                
        for i in range(1,m):
            temp = [] 
            prev = 0
            for j in range(n):
                if not (obstacleGrid[i][j]):
                    temp.append(prev +  res[j])
                else:
                    temp.append(0)
                prev = temp[j]
            res = temp
        return res[-1]