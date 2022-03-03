class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        memo, result = [0] * len(nums), 0
        for i in range(2, len(nums)):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                memo[i] = memo[i-1] + 1
            result += memo[i]
        return result