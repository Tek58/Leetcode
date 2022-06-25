class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        count_right = 0
        inc = nums[0]
        count_left = 0
        for i in range(1, len(nums)):
            if nums[i] >= inc:
                inc = nums[i]
            else:
                count_right += 1
        
        if count_right <= 1:
            return True
            
        dec  = nums[len(nums)-1]        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= dec:
                dec = nums[i]
            else:
                count_left += 1
            
        return count_left <= 1