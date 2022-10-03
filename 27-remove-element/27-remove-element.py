class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] < val:
                i += 1
                continue
            elif nums[i] == val:
                nums.remove(val)
            else:
                break
        return len(nums)