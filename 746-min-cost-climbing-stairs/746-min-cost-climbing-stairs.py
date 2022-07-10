class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] = min(cost[i-2]+cost[i] , cost[i-1]+cost[i] )
        return min(cost[-2], cost[-1])
    
        # @cache
        # def dp(i):
        #     if i < 0:
        #         return 0
        #     return min(dp(i-1) + cost[i], dp(i-2) + cost[i])
        # return min(dp(len(cost) -1), dp(len(cost) -2))