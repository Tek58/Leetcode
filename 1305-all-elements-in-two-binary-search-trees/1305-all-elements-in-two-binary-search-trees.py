# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result1 = []
        result2 = []
        def inline(root, result):
            if not root:
                return
            inline(root.left, result)
            result.append(root.val)
            inline(root.right, result)
        inline(root1, result1)
        inline(root2, result2)
        totalRes = result1 + result2
        res = sorted(totalRes)
        return res
        