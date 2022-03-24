class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) == r and len(mat[0]) == c:
            return mat
        if len(mat) * len(mat[0]) != r*c:
            return mat
        
        new_matrix = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                new_matrix.append(mat[i][j])
        
        result = []
        col = 0
        for i in range(r): 
            temp = []
            for j in range(c):
                temp.append(new_matrix[col])
                col += 1
            result.append(temp)
            
        return result
        