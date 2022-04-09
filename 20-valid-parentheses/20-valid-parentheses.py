class Solution:
    def isValid(self, s: str) -> bool:
        parentesis = { '(' : ')', '{' : '}', '[' : ']' }
        stack = []
        for i in s:
            if i in parentesis:
                stack.append(i)
            else:
                if stack and parentesis[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return True if not stack else False