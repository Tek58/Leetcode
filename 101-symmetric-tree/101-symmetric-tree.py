# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)
    
    def helper(self, left_node, right_node):
        if not right_node or not left_node:
            return right_node == None and left_node == None
        if right_node.val != left_node.val:
            return False
        val1 = self.helper(left_node.left, right_node.right)
        val2 = self.helper(left_node.right, right_node.left)
        return val1 and val2