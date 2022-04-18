# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = []
        self._helper(root, result)
        return result[k-1]
    def _helper(self, root, result):
        if not root:
            return
        self._helper(root.left, result)
        result.append(root.val)
        self._helper(root.right, result)
        