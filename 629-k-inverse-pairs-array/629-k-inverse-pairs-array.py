class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        MOD = 10 ** 9 + 7
        for i in range(1, n + 1):
            curr = 0
            for j in range(k + 1):
                curr += dp[i - 1][j]
                if j >= i:
                    curr -= dp[i - 1][j - i]
                dp[i][j] = (dp[i][j] + curr) % MOD
        return dp[n][k]