class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        store = Counter(nums)
        res = []
        def backtracking(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in store:
                count = store[num]
                if count > 0:
                    curr.append(num)
                    store[num] -= 1
                    backtracking(curr)
                    
                    curr.pop()
                    store[num] += 1
                    
        backtracking([])
        return res
                
                    