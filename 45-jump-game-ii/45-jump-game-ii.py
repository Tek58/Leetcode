class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l , r = 0, 0
        while r < len(nums) - 1:
            curr = 0
            for i in range(l, r + 1):
                curr = max(curr, i + nums[i])
            l = r + 1
            r = curr
            res += 1
        
        return res 
            