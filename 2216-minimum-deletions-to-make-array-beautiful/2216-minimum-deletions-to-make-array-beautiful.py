class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if (i + count) % 2 == 0:
                if i + 1 < len(nums) and nums[i] == nums[i+1]:
                    count += 1
        return count + 1 if (len(nums) - count) % 2 == 1 else count 