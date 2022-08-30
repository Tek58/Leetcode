class Solution:
    def countAsterisks(self, s: str) -> int:
        between = False
        count = 0
        for char in s:
            if char == "|":
                between = not between
                
            if char == "*" and not between:
                count += 1
                
        return count