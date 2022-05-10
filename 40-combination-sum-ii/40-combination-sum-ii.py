class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(index, temp, total):
            if total == target:
                res.append(temp[:])
                return
            if total > target:
                return
            
            prev = -1
            for i in range(index, len(candidates)):
                curr = candidates[i]
                if curr == prev:
                    continue
                
                temp.append(curr)
                backtracking(i+1, temp, total + curr)
                temp.pop()
                prev = curr
            
        backtracking(0, [], 0)
        return res
        