class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:    
        first = strs[0]
        i = 0
        while i < len(first):
            for j in range(1,len(strs)):
                if i > len(strs[j]) - 1 or strs[j][i] != first[i]:
                    return "" if i == 0 else first[:i]
            i += 1
        
        return "" if i == 0 else first[:i]
        
                
                
            