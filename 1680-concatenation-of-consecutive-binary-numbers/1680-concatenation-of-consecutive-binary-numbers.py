class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = ""
        for i in range(1, n+1):
            result += (bin(i)[2:])
        val = int(result,2)
        
        return val % (10**9 + 7)