class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        currSum = 0
        for num in nums:
            if num % 2 == 0:
                currSum += num
                
        for i in queries:
            val, id = i
            if nums[id] % 2 == 0:
                currSum -= nums[id]
            nums[id] += val
            if nums[id] % 2 == 0:
                currSum += nums[id]
            res.append(currSum)
            
        return res 