class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result= 0
        prevDiff = inf
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                val = nums[i] + nums[left] + nums[right]
                diff = abs(target - val)
                if diff == 0:
                    return val
                if diff < prevDiff:
                    prevDiff = diff
                    result = val
                if val < target:
                    left += 1
                else:
                    right -= 1
        return result
                
            

        
                    