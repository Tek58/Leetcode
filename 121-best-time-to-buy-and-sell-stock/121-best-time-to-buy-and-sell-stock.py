class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyingDayIndex = 0
        for sellingDayIndex in range(len(prices)):
            if prices[sellingDayIndex] <= prices[buyingDayIndex]:
                buyingDayIndex = sellingDayIndex
            else:
                maxProfit = max(maxProfit, (prices[sellingDayIndex] - prices[buyingDayIndex]))
        return maxProfit            