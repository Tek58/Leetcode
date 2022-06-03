class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = []
        for i in range(len(self.matrix)):
            sumContainer = 0
            temp = []
            for j in range(len(self.matrix[0])):
                sumContainer += self.matrix[i][j]
                temp.append(sumContainer)
            self.prefix.append(temp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        result = 0
        for i in range(row1, row2 +1):
            if col1 != 0:
                result += (self.prefix[i][(col2)] - self.prefix[i][(col1-1)])
            else:
                result += (self.prefix[i][(col2)])
        return result
                


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)