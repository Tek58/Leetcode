class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num = 2
        while num <= n:
            num *= 2
        return num - 1 - n