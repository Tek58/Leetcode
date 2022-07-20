class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        @lru_cache(None)
        def exists(char, index):
            return s.find(char, index)

        def isSubsequence(word):
            index = -1
            for ch in word:
                index = exists(ch, index + 1)
                if index == -1:
                    return False
            return True

        count = 0
        for word in words:
            if isSubsequence(word):
                count+= 1
        return count