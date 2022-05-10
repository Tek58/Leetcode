class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(num, curr, total):
            if len(curr) == k and total == 0:
                res.append(curr[:])
                return
            
            if total < 0 or len(curr) > k:
                return
            
            for i in range(num+1, 10):
                curr.append(i)
                dfs(i, curr, total - i)
                curr.pop()
                
        dfs(0, [], n)
        return res
        
                