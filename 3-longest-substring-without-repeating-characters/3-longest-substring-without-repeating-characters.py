class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Max = 0
        visited = set()
        first = 0
        second = 0
        while second < len(s):
            if s[second] in visited:
                Max = max(Max, (second - first))
                while s[first] != s[second]:
                    visited.remove(s[first])
                    first += 1
                first += 1
                
            visited.add(s[second])
            second += 1
        Max = max(Max, (second - first))
        return Max
                
                
            