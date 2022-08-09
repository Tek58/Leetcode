class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = [1] * len(arr)
        seen = set(arr)
        for i in range(1,len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    currNum = arr[i] // arr[j]
                    if currNum in seen:
                        currNumIndex = arr.index(currNum)
                        dp[i] += dp[j] * dp[currNumIndex]
        
        return sum(dp) % MOD
                        
        