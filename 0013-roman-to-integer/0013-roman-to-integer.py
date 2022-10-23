class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumbers = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        res = 0
        for i in range(len(s)-1):
            first = romanNumbers[s[i]]
            second = romanNumbers[s[i + 1]]
            if first < second:
                res -= first
            else:
                res += first
            
        return res + romanNumbers[s[-1]]
            

# Time Complexity O(n)
# Space Complixity O(1)
        