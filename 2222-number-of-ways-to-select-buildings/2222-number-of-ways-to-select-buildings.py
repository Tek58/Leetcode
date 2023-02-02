class Solution:
    def numberOfWays(self, s: str) -> int:
        store = [[0, 0], [0, 0]]
        res = 0
        for i in range(len(s)):
            curr = int(s[i])
            res += store[1][1 - curr]
            store[1][curr] += store[0][1 - curr]
            store[0][curr] += 1
        
        return res
        
        