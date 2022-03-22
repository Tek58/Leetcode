class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        for index, num in enumerate(nums):
            wanted_num = target - num
            if wanted_num in store:
                return [store[wanted_num], index]
            store[num] = index 