class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join([str(digit) for digit in digits])
        num = str(int(num) + 1)
        res = list(num)
        return res