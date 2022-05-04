class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        container = defaultdict(int)
        count = 0
        for i in nums:
            val = k - i
            if container[val] > 0:
                count += 1
                container[val] -= 1
            else:
                container[i] += 1
        
        return count