class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = ""
        for word in words:
            newWord = word[::-1]
            result += newWord + " "
        return result[:-1]
        