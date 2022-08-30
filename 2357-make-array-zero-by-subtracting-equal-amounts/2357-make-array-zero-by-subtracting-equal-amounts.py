class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        count = 0
        for i in nums:
            if i not in seen and i != 0:
                count += 1
                seen.add(i)
        
        return count
        