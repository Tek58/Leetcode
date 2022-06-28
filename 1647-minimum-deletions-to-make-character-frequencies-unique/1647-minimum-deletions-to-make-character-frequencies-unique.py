class Solution:
    def minDeletions(self, s: str) -> int:
        store = Counter(s).values()
        print(store)
        visited = set()
        result  = 0 
        mx = float("-inf") 
        for val in store:
            while val and val in visited:
                val -= 1
                result += 1
            if val:
                visited.add(val)
        return result 
            
            