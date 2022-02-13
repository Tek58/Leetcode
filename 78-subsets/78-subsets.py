class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.solve( 0, [], nums, ans)
        return ans
        
    def solve(self, idx, subset, nums, ans):
        if idx == len(nums):
            ans.append(subset[:])
        else:
            subset.append(nums[idx])
            self.solve( idx + 1, subset, nums, ans)
            subset.pop()
            self.solve( idx + 1, subset, nums, ans)
