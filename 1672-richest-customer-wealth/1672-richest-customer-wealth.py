class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = -1
        for i in accounts:
            maxWealth = max(maxWealth, sum(i))
        return maxWealth