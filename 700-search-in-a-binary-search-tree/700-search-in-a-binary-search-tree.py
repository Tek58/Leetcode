# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not node:
            return 
        if val == node.val:
            return node
        elif val < node.val:
            return self.searchBST(node.left, val)
        else:
            return self.searchBST(node.right, val)
        