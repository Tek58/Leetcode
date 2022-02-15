class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        container = Counter(nums)
        
        for key, val in container.items():
            if val == 1:
                return key
            
        