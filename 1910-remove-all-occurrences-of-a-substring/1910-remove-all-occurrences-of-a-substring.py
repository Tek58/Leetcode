class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= len(part):
                curr = stack[-len(part):]
                currVal = ''.join(curr)
                if currVal == part:
                    # stack = stack[-len(part):]z
                    count = 0
                    while count < len(part):
                        stack.pop()
                        count += 1
        return ''.join(stack) if stack else ''
                