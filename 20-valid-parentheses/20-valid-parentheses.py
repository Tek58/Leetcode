class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = set(["(","{", "["])
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if len(stack) != 0:
                    curr = stack[-1]
                    if ( i == ')' and curr == '(' ) or  ( i == '}' and curr == '{' ) or ( i == ']' and curr == "[" ):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0