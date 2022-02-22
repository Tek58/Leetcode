class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        val = [i for i in range(1, 27)]
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        d = dict(zip(letters, val))
        for ch in columnTitle:
            res = res * 26 + d[ch]
        return res