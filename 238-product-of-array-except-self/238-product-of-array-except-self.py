class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix = [1]
        right_prefix = [1]
        for i in nums:
            left_prefix.append(left_prefix[-1]*i)
        
        for i in range(len(nums)-1, -1, -1):
            right_prefix.append(right_prefix[-1]*nums[i])
            
        right_prefix.reverse()
        
        res = []
        for i in range(len(nums)):
            leftVal = left_prefix[i]
            rightVal = right_prefix[i+1]
            res.append(leftVal * rightVal)
        
        return res