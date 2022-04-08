class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = localMax = float("-inf")
        for i in nums:
            localMax = max(i, i + localMax)
            globalMax = max(globalMax, localMax)
        return globalMax