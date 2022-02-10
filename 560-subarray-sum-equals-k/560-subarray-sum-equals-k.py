class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        container = {0:1}
        current = 0
        counter = 0
        for i in nums:
            val = current+i
            if val - k in container:
                counter += container[val - k]
            if val not in container:
                container[val] = 1
            else:
                container[val] += 1
            current += i

        return counter