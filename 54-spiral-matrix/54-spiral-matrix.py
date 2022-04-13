class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        topLeft = (0,0)
        topRight = (0, len(matrix[0])-1)
        bottomLeft = (len(matrix)-1, 0)
        bottomRight = (len(matrix)-1, len(matrix[0])-1)
        count = len(matrix) * len(matrix[0])
        while len(res) < count:
            for i in range(topLeft[1], topRight[1]+1):
                if len(res) == count:
                    break
                res.append(matrix[topLeft[0]][i])
                print(topLeft[0], i, res)
            for i in range(topRight[0]+1, bottomRight[0]+1):
                if len(res) == count:
                    break
                res.append(matrix[i][topRight[1]])
                print(i, topRight[1], res)
            for i in range(bottomRight[1] - 1, bottomLeft[1], -1 ):
                if len(res) == count:
                    break
                res.append(matrix[bottomRight[0]][i])
                print(bottomRight[0], i, res, bottomRight, bottomLeft, "l")
            for i in range(bottomLeft[0], topLeft[0], -1):
                if len(res) == count:
                    break
                res.append(matrix[i][bottomLeft[1]])
                print(i, bottomLeft[1], res, "kk")
            
            topLeft = (topLeft[0]+1, topLeft[1]+1)
            topRight= (topRight[0]+1, topRight[1]-1)
            bottomRight = (bottomRight[0]-1, bottomRight[1]-1)
            bottomLeft = (bottomLeft[0]-1, bottomLeft[1]+1)
            
        return res