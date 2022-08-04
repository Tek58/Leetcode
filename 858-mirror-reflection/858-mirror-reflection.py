class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        extention = q 
        reflection = p
        while extention % 2 == 0 and reflection % 2 == 0:
            extention //= 2
            reflection //= 2
        
        if extention % 2 == 0 and reflection % 2 != 0:
            return 0
        if extention % 2 != 0 and reflection % 2 == 0:
            return 2
        if extention % 2 != 0 and reflection % 2 != 0:
            return 1
        
        return -1