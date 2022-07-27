# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution(object):
    def __init__(self):
        self.prev_res = None
        
    def flatten(self, root):
        def inorder(node):
            if not node:
                return
            inorder(node.right)
            inorder(node.left)
            node.right = self.prev_res
            node.left = None
            self.prev_res = node
            
        inorder(root)
        