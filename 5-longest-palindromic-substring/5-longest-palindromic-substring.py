class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        longestLen = 0
        def isPalindrome(left, right):
            nonlocal longest, longestLen
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > longestLen:
                    longest = s[left:right+1]
                    longestLen = right - left + 1
                left -= 1
                right += 1
                
        for i in range(len(s)):
            isPalindrome(i, i)
            isPalindrome(i, i + 1)
            
        return longest