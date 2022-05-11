class Solution:
    def intToRoman(self, num: int) -> str:
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        symbols = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = []
        for i, v in enumerate(values):
            res.append((num//v) * symbols[i])
            num %= v
        return ''.join(res)