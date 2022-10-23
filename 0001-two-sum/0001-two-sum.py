class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = defaultdict(int)
        for i in range(len(nums)):
            wanted = target - nums[i]
            if wanted in store:
                return [store[wanted], i]
            store[nums[i]] = i