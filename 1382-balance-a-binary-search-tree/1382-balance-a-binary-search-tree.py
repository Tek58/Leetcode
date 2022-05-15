# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res=[]
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
            
        def balance(l, r):
            if l<=r:
                mid = (l+r)//2
                cur = TreeNode(res[mid])
                cur.left = balance(l, mid-1)
                cur.right = balance(mid+1, r)
                return cur

        inorder(root)
        return balance(0, len(res)-1)
        