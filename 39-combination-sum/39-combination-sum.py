class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(index, temp, total):
            if total == target:
                res.append(temp[:])
                return
            
            if index >= len(candidates) or total > target:
                return
            
            temp.append(candidates[index])
            dfs(index, temp, total + candidates[index])
            temp.pop()
            dfs(index + 1, temp, total)
            
        dfs(0, [], 0)
        return res