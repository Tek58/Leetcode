class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        def helper(total, n, k):
            if n <= 0 and total == target:
                return 1
            elif n <= 0:
                return 0
            elif (total, n) in memo:
                return memo[(total, n)]
            else:
                memo[(total, n)] = 0
                for i in range(1, k + 1):
                    memo[(total, n)] += helper(total + i, n - 1, k)
                return memo[(total, n)]
        return helper(0, n, k) % (10**9 + 7)  