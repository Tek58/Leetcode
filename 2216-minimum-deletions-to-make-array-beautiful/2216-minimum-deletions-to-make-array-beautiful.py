class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            if (i + count) % 2 == 0:
                if i + 1 < n and nums[i] == nums[i+1]:
                    count += 1
        return count + 1 if (n - count) % 2 == 1 else count 