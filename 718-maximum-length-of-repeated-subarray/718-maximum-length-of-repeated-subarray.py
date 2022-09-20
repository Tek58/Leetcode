class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[0]*(n+1) for i in range(m+1) ]
        
        counter = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums2[i-1] == nums1[j-1]:
                    diagonal = dp[i-1][j-1]
                    dp[i][j] += (diagonal + 1)
                    counter = max(counter, dp[i][j])
                    
        return counter
                