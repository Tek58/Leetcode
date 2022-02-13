class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        start = (2**(len(nums))) + 1
        end = 2**(len(nums) + 1)
        for i in range(start, end):
            temp = []
            val = bin(i)[3:]
            for i in range(len(val)):
                if val[i] == "1":
                    temp.append(nums[i])
            result.append(temp)
        return result
                
                
            