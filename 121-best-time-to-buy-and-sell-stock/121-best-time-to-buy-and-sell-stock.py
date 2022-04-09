class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        maxProfit = 0
        buyingDayIndex = 0
        sellingDayIndex = 1
        while sellingDayIndex < len(prices):
            if prices[sellingDayIndex] <= prices[buyingDayIndex]:
                buyingDayIndex = sellingDayIndex
            else:
                maxProfit = max(maxProfit, (prices[sellingDayIndex] - prices[buyingDayIndex]))
            sellingDayIndex += 1
        return maxProfit            