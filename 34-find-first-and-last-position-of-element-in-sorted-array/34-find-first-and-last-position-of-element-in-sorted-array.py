class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fIndex, first = -1, False
        sIndex = -1
        for i in range(len(nums)):
            found = nums[i] == target
            if not first and found:
                fIndex = i
                first = True
            
            if first and found:
                sIndex = i
        
        return [fIndex, sIndex]
                
                