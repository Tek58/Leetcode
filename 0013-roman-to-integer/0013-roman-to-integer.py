class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        romanNumbers = {"O": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        specialNumbers = { "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900 }
        s += "O"
        index = 0
        res = 0
        while index < n:
            first = s[index]
            second =s[index + 1]
            curr = first + second
            if curr in specialNumbers:
                res += specialNumbers[curr]
                index += 1
            else:
                res += romanNumbers[first]
            index += 1
        return res
            
