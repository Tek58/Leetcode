class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        container = { "2" : ["a","b","c"], "3" : ["d","e","f"], "4" : ["g","h","i"], "5" : ["j","k","l"] , "6" : ["m","n","o"] , "7" : ["p","q","r","s"] , "8" : ["t","u","v"] , "9" : ["w","x","y","z"] }
        result = []
        if len(digits) == 0:
            return result
        
        if len(digits) == 1:
            return list(container[digits[0]])
        
        prev = self.letterCombinations(digits[:-1])
        additional = container[digits[-1]]
        for let1 in prev:
            for let2 in additional:
                result.append(let1 + let2)
        return result
        
        