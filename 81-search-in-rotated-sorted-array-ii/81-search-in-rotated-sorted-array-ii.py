class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        index = 0
        result = []
        for i in range(len(nums)- 1 ):
            if nums[i+1] < nums[i]:
                index = i +1
                break
        for i in range(index, len(nums)):
            result.append(nums[i])
        for i in range(index):
            result.append(nums[i])
        left = 0
        
        right = len(result) - 1
        while left <= right:
            mid  = left + (right - left)//2
            if result[mid] == target:
                return True
            if target< result[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False