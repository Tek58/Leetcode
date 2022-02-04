class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index = {0: -1}
        balance = maxlen = 0
        for i, num in enumerate(nums):
            balance += num - 0.5
            maxlen = max(maxlen, i - index.setdefault(balance, i))
        return maxlen