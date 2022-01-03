class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        store = defaultdict(int)
        trusted = defaultdict(int)
        for i in trust:
            store[i[0]] += 1
            trusted[i[1]] += 1       
        
        for i in range(1, n+1):
            if store[i] == 0 and trusted[i] == n-1:
                return i
        return -1