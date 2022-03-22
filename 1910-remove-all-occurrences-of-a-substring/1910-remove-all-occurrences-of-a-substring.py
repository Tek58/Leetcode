class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s
#         stack = []
#         for i in s:
#             if len(stack) < len(part):
#                 stack.append(i)
#             else:
#                 stack = self.checkAndRemove(stack, part)
        
#         return ''.joint(stack)
    
#     def chechAndRemove(stack, part):
#         left = 0
#         right = 0
#         newStack = []
#         while right < len(part):
#             if (right - left)+1 == len(part):
#                 newStack = [stack[:left] + stack[right+1:]]
#             else:
                
#             right += 1
#         return newStack
                