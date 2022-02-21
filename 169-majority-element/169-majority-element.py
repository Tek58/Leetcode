class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = Counter(nums)
        result = []
        for key, val in store.items():
            if val >= len(nums)/2:
                return key