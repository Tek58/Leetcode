class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.lower():
            return True
        capitals = 0
        first = -1
        for i in range(len(word)):
            curr = word[i]
            if curr.isupper():
                capitals += 1
                first = i
        if (capitals == 1 and first == 0) or capitals == len(word) :
            return True
        return False
        