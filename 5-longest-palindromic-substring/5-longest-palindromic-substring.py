class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        longestLen = 0
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > longestLen:
                    longest = s[left:right+1]
                    longestLen = right - left + 1
                left -= 1
                right += 1
            
            left , right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > longestLen:
                    longest = s[left:right+1]
                    longestLen = right - left + 1
                left -= 1
                right += 1
            
        return longest
            
            