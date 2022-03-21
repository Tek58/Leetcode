class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = defaultdict(int)
        for num in nums:
            if num in store:
                return True
            store[num] += 1
        return False