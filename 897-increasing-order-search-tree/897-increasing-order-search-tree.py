# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        def inorderTraversal(node):
            if not node:
                return None
            inorderTraversal(node.left)
            inorder.append(node.val)
            inorderTraversal(node.right)
        inorderTraversal(root)
        ans = cur = TreeNode(None)
        for v in inorder:
            cur.right = TreeNode(v)
            cur = cur.right
            
        return ans.right