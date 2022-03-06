class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        for i in range(2, n+1):
            curr = i*(2*i-1)
            res *= curr
        return res % (10**9 + 7)