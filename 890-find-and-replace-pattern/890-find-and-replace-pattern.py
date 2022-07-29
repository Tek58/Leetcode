class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        newPattern = self.Pattern(pattern)
        return [word for word in words if(self.Pattern(word) == newPattern)]


    def Pattern(self, pattern):
        container = {}
        result = ""


        for i in range(len(pattern)):
            if pattern[i] in container:
                container[i] = container[pattern[i]]
            else:
                container[pattern[i]] = i
        
        for i in container.values():
            result += str(i)
        
        return result
            