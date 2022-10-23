class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:    
        s1 = min(strs)
        s2 = max(strs)
        
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        
        return s1
    
# Time Compexity O(n * m) n = len(strs) m = len(strs[i])
# Space Complexity O(1)