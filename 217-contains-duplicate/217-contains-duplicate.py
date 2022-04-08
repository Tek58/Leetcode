class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = Counter(nums)
        for val in store.values():
            if val >= 2:
                return True
        return False