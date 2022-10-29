class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)

# Time: O(N)
# Space: O(1) without the sorting