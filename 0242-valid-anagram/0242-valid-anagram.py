class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)
        for key, value in tCount.items():
            if sCount[key] < value:
                return False
        return len(s) == len(t)
    
# Time: O(N + M)
# Space: O(N + M)