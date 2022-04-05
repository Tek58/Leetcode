class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        store = defaultdict(int)
        maxNum = nums[0]
        for i in nums:
            store[i] += i
            maxNum = max(maxNum, i)
            
        @cache
        def maxPoint(num):
            if num == 0:
                return 0
            if num == 1:
                return store[1]
            return max(maxPoint(num-1), maxPoint(num-2) + store[num])
        
        return maxPoint(maxNum)
        
