class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[-10**20] * (m + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(i + 1):
                if i  == 0:
                    dp[i][j] = 0
                
                right = n + j - i - 1
                curr = dp[j][i] + nums[j] * multipliers[i]
                if curr > dp[j + 1][i + 1]:
                    dp[j + 1][i + 1] = curr
                
                curr = dp[j][i] + nums[right] * multipliers[i]
                if curr > dp[j][i + 1]:
                    dp[j][i + 1] = curr
        
        return max(dp[i][m] for i in range(m + 1))
                