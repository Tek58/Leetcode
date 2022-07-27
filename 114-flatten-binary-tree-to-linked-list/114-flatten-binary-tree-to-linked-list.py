# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution(object):        
    def flatten(self, root):
        if root:
            stack = [root]
            while len(stack):
                root = stack.pop()
                if root.right: 
                    stack.append(root.right)
                if root.left: 
                    stack.append(root.left)

                root.left = None
                root.right = stack[-1] if len(stack) else None