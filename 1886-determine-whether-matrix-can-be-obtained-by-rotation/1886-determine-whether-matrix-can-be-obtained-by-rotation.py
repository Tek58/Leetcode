class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        res = False
        n = len(mat)
        
        for _ in range(4):
            if mat == target:
                res = True
                break

            for i in range(n):
                for j in range(i, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
                    
            for i in range(n):
                left = 0
                right = n - 1
                while left < right:
                    mat[i][left], mat[i][right] = mat[i][right], mat[i][left]
                    left += 1
                    right -= 1
                    
        return res