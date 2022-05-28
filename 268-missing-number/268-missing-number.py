class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        currSum = sum(nums)
        overallSum = (n * (n + 1)) // 2
        return overallSum - currSum