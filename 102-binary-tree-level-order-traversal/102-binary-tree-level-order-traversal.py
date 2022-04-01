# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        stack = [root]
        self.helper(result, stack)
        return result
        
    def helper(self,result, stack):
        res = []
        for i in stack:
            res.append(i.val)
        if res:
            result.append(res)
        if len(stack) == 0:
            return 
        
        length = len(stack)
        for i in range(length):
            element = stack.pop(0)
            if element.left:
                stack.append(element.left)
            if element.right:
                stack.append(element.right)
        self.helper(result, stack)
                    
        