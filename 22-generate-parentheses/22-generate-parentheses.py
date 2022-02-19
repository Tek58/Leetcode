class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def backtracking(openCount, closeCount):
            if openCount == closeCount == n:
                result.append(''.join(stack))
                return
            
            if openCount < n:
                stack.append("(")
                backtracking(openCount + 1, closeCount)
                stack.pop()
            
            if closeCount < openCount:
                stack.append(")")
                backtracking(openCount, closeCount + 1)
                stack.pop()
        
        backtracking(0, 0)
        return result