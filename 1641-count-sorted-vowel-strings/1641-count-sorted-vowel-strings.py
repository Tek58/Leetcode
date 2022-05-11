class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [0, 1, 1, 1, 1, 1]
        for i in range(1, n + 1):
            for k in range(1, 6):
                dp[k] += dp[k - 1]
        return dp[5]
    