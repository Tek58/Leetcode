class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len)
        words = reversed(words)
        result = ''
        for word in words:
            curr = word + '#'
            if curr not in result:
                result += curr
                
        return len(result)