class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return 0
        res = float('-inf')
        m, n = len(matrix), len(matrix[0])
        
        for i in range(n):
            sums = [0 for _ in range(m)]
            for j in range(i, n):
                for l in range(m):
                    sums[l] += matrix[l][j]
                curr = [0]
                temp, max_sum = 0, float('-inf')
                for item in sums:
                    temp += item
                    target = temp - k 
                    left = bisect.bisect_left(curr, target)
                    if left < len(curr):
                        max_sum = max(max_sum, temp - curr[left])
                    bisect.insort(curr, temp)

                res = max(res, max_sum)
        return res