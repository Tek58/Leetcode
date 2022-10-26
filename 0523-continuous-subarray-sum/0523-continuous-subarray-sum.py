class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [nums[0]]
        visited = set()
        for i in range(1,len(nums)):
            val = prefix[i - 1] + nums[i]
            prefix.append(val)
            
        for i in range(len(prefix)):
            prefix[i] = prefix[i] % k
        
        prev = 0
        for i in range(len(prefix)):
            if prefix[i] in visited:
                return True
            visited.add(prev)
            prev = prefix[i]
            
        return False