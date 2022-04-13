class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        topLeft = curr = (0,0)
        topRight = (0, n-1)
        bottomLeft = (n-1, 0)
        bottomRight = (n-1, n-1)
        count = 1
        while count <= n*n:
            for i in range(topLeft[1], topRight[1]+1):
                matrix[topLeft[0]][i] = count
                count += 1
            for i in range(topRight[0]+1, bottomRight[0]+1):
                matrix[i][topRight[1]] = count
                count += 1
            for i in range(bottomRight[1] - 1, bottomLeft[1]-1, -1 ):
                matrix[bottomRight[0]][i] = count
                count += 1
            for i in range(bottomLeft[0] - 1, topLeft[0], -1):
                matrix[i][bottomLeft[1]] = count
                count += 1
            
            topLeft = curr = (topLeft[0]+1, topLeft[1]+1)
            topRight= (topRight[0]+1, topRight[1]-1)
            bottomRight = (bottomRight[0]-1, bottomRight[1]-1)
            bottomLeft = (bottomLeft[0]-1, bottomLeft[1]+1)
        return matrix
