class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        for letter in s:
            if letter.isalpha() or letter.isnumeric():
                word += letter.lower()
        
        left = 0
        right = len(word) - 1
        while left <= right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True