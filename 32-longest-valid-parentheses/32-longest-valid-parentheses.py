class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        maxLen = 0
        for i in s:
            if i == '(':
                stack.append(0)
            else:
                if len(stack) > 1:
                    curr = stack.pop()
                    stack[-1] += curr + 2
                    maxLen = max(maxLen, stack[-1])
                else:
                    stack = [0]

        return maxLen