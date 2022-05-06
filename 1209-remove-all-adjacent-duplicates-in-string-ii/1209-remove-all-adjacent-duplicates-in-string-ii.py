class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if not stack:
                stack.append([i,1])
            else:
                if stack[-1][0] == i:
                    stack[-1][1] += 1
                if stack[-1][0] != i:
                    stack.append([i,1])
                if stack[-1][1] == k:
                    stack.pop()
        # print(stack)
        lis = []
        for i in stack:
            for j in range(i[1]):
                lis.append(i[0])
        return "".join(lis)