class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [(s[0], 1)]
        for i in range(1, len(s)):
            if not stack:
                stack.append((s[i], 1))
                continue
            curr, val = stack.pop()
            if curr == s[i]:
                if val + 1 < k:
                    res = (curr, val + 1)
                    stack.append(res)
            else:
                stack.append((curr, val))
                stack.append((s[i], 1))
            
        result = ''
        for i in stack:
            result += i[0] * i[1]
        
        return result
        