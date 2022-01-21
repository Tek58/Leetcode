class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, total, Min = 0, 0, sys.maxsize
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < Min:
                start = (i + 1)%len(gas)
                Min = total
        return start