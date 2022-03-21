class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = globalMax = float('-inf')
        for num in nums:
            localMax = max(num, localMax + num) 
            globalMax = max(globalMax, localMax)
        return globalMax