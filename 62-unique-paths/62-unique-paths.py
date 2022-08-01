class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [1] * n
        for i in range(m-1):
            temp = [1] * n
            for j in range(n-2, -1,-1):
                temp[j] = temp[j+1] + res[j]
            res = temp
        return res[0]
                
            