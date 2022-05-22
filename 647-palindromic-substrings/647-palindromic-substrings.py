class Solution:
    def countSubstrings(self, s: str) -> int:
        size, counter = len(s), 0
        
        for idx in range(size):
            for left_c, right_c in ( (idx, idx), (idx, idx+1) ):
                while left_c >= 0 and right_c < size and s[left_c] == s[right_c]:
                    counter += 1
                    left_c, right_c = left_c - 1, right_c + 1
                    
        return counter