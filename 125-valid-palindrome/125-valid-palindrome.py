class Solution:
    def isPalindrome(self, s: str) -> bool:
        newWord = []
        for i in s:
            if i.isalpha() or i.isnumeric():
                newWord.append(i.lower())
        processedWord = ''.join(newWord)
        left = 0
        right = len(processedWord) - 1
        while left <= right:
            if processedWord[left] != processedWord[right]:
                return False
            left += 1
            right -= 1
        return True
                