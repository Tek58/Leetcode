class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(i) for i in set(permutations(nums))]
                
                    