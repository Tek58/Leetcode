class Solution(object):
    def removeDuplicateLetters(self, s):
        count = [0] * 26
        visited = set()
        stack = []
        for i in s:
            count[ord(i)-97] += 1
            
        for character in s:
            count[ord(character)- ord('a')] -= 1
            val = ord(character) - ord('a')
            if val not in visited:
                while stack and character<stack[-1] and count[ord(stack[-1]) - ord('a')] >0:
                    visited.remove((ord(stack[-1]) - ord('a')))
                    stack.pop()
                stack.append(character)
                visited.add(val)

        return ''.join(stack)
