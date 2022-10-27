class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        n = len(digits)
        for i in range(n):
            num += digits[i] * pow(10, n - i - 1)
        return [int(i) for i in str(num + 1)]