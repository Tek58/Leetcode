class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        
        i = j = float("inf")
        for num in nums:
            i = min(i, num)
            if num > j:
                return True
            elif num > i:
                j = num
                
        return False
