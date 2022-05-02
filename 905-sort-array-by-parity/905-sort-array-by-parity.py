class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        even = 0
        odd = len(nums)-1
        for i in nums:
            # print(i, even, odd)
            if i % 2 == 0:
                res[even] = i
                even += 1
            else:
                res[odd] = i
                odd -= 1
        return res