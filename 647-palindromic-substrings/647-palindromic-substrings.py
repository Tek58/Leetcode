class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        
        for i in range(len(s)):
            for j in range(2):
                left_c, right_c = i, i + j
                while left_c >= 0 and right_c < len(s) and s[left_c] == s[right_c]:
                    counter += 1
                    left_c, right_c = left_c - 1, right_c + 1
                    
        return counter