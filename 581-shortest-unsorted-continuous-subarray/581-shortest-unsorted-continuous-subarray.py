class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lower, upper = len(nums)-1, 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>nums[i]:
                lower = min(lower, stack.pop())
            stack.append(i)
        
        stack = []        
        for i in range(len(nums)-1,-1, -1):
            while stack and nums[stack[-1]]<nums[i]:
                upper = max(upper, stack.pop())
            stack.append(i)
            
        if lower >= upper:
            return 0
        return upper - lower + 1