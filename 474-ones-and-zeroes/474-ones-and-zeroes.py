class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        store = []
        for i in strs:
            res = [i.count("0"), i.count("1")]
            store.append(res)
            
        @lru_cache(None)
        def dp(i, m, n):
            if i == len(strs):
                return 0
            
            ans = dp(i+1, m, n)
            zeros = store[i][0]
            ones = store[i][1]
            if m >= zeros and n >= store[i][1]:
                ans = max(ans, dp(i + 1, m - zeros, n - ones) + 1)
                
            return ans
        
        return dp(0, m, n)
            