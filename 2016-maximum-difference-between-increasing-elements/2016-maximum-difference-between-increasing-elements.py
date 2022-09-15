class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = 0
        for i in range(len(nums)-1):
            if(max(nums[i:]) != i):
                maxDiff = max(maxDiff, max(nums[i::])-nums[i])
        if not maxDiff:
            return -1
        return maxDiff