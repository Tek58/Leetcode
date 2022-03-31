class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isValidCeiling(ceiling):
            count, total = 1, 0  
            for i in range(len(nums)):
                if total + nums[i] <= ceiling:
                    total += nums[i] 
                else:
                    total = nums[i]  
                    count += 1
                if (count > m):
                    return False 
            return True 

        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if isValidCeiling(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left