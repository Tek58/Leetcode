class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        SumCounter = 0
        for i in range(1,len(prices)):
            val = (prices[i] - prices[i-1])
            if val > 0:
                SumCounter += val
                
        return SumCounter
            