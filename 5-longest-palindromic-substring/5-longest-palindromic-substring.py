class Solution:
    def __init__(self):
        self.longest = ""
        self.longestLen = 0
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > self.longestLen:
                    self.longest = s[left:right+1]
                    self.longestLen = right - left + 1
                left -= 1
                right += 1
                
        for i in range(len(s)):
            isPalindrome(i, i)
            isPalindrome(i, i + 1)
            
        return self.longest