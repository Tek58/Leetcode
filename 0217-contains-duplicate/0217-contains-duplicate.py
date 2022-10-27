class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not (len(nums) == len(list(set(nums))))
    
# Time: O(N)
# Space: O(1)
        