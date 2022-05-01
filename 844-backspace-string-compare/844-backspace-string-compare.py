class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stack(s, stack):
            for char in s:
                if char is not "#":
                    stack.append(char)
                else:
                    if not stack:
                        continue
                    stack.pop()
            return stack

        l1 = stack(s, [])
        l2 = stack(t, [])
        return l1 == l2
        
    
        