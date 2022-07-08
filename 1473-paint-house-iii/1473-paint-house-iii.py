class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def dp(idx, prev_color, k):
            if idx >= m:
                if k == 0:
                    return 0
                return -1
                    
            if k < 0:
                return -1

            if houses[idx] != 0:
                curr = 0 if prev_color == houses[idx] else 1
                return dp(idx + 1, houses[idx], k - curr)

            best = -1
            for new_color in range(1, n + 1):
                new_color_cost = cost[idx][new_color - 1]
                val = 0 if prev_color == new_color else 1
                other_costs = dp(idx + 1, new_color, k - val)

                if other_costs >= 0:
                    best = min(best if best > 0 else float("inf"), new_color_cost + other_costs)
            return best


        return dp(0, 0, target)