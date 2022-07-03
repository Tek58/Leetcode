class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = 0
        if len(nums) == 1 or len(nums) == nums.count(nums[0]):
            return (1)
        
        prev = nums[1] - nums[0]
        if (prev != 0):
            length += 2
        else:
            length += 1
        
        for i in range(2, len(nums)):
            if (prev <= 0 and nums[i] - nums[i - 1] > 0):
                prev = nums[i] - nums[i - 1]
                length += 1
                
            elif (prev >= 0 and nums[i] - nums[i - 1] < 0):
                prev = nums[i] - nums[i - 1]
                length += 1
        
        return length
