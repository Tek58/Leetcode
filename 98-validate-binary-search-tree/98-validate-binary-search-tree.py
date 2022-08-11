# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        res = []
        def helper(node):
            if not node:
                return 
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        count = Counter(res)
        return res == sorted(res) and len(count) == len(res)
        