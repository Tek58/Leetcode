class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string_one = ''.join(word1)
        string_two = ''.join(word2)
        return string_one == string_two