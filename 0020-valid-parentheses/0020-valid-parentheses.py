class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {'(' : ')', '{': '}', '[': ']'}
        stack = []
        for cha in s:
            if cha in parenthesis:
                stack.append(cha)
            else:
                if stack:
                    top = stack.pop()
                    if parenthesis[top] != cha:
                        return False
                else:
                    return False
        
        return True if not stack else False