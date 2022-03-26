class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        return self._helper(nums,left, right ,target)
        
    def _helper(self,nums, left, right, target):
        if right >= left:
            mid = (right + left)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
                return self._helper(nums, left,right, target)
            elif target > nums[mid]:
                left = mid + 1
                return self._helper(nums,left, right, target)
        return -1