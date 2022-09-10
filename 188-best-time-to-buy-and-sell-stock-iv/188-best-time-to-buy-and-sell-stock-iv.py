class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0]* len(prices)
        
        for t in range(k):
            position = -prices[0]
            profit = 0
            for i in range(1, len(prices)):
                position = max(position, dp[i] - prices[i])
                profit = max(profit, position + prices[i])
                dp[i] = profit
        
        return dp[-1]