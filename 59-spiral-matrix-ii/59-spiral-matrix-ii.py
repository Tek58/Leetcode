class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        top, bottom = 0, n
        count = 1
        while count <= n*n:
            for i in range(top, bottom):
                matrix[top][i] = count
                count += 1
            for i in range(top + 1, bottom):
                matrix[i][bottom-1] = count
                count += 1
            for i in range(bottom - 2, top - 1 , -1 ):
                matrix[bottom-1][i] = count
                count += 1
            for i in range(bottom - 2, top, -1):
                matrix[i][top] = count
                count += 1
            
            top += 1
            bottom -= 1
        return matrix
    