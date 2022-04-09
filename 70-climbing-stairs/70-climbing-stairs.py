class Solution:
    def climbStairs(self, n: int) -> int:
        memo = { 0: 1, 1:1 }
        def dp(i):
            if i not in memo:
                memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        return dp(n)
        