# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            node = TreeNode(val)
            root = node
            return root
        self.recurseInsert(root, val, None)
        return root
        
    
    def recurseInsert(self,root,val,parent):
        if root is None :
            node = TreeNode(val)
            if node.val < parent.val:
                parent.left = node
            else:
                parent.right = node
            return 
        elif val < root.val :
            self.recurseInsert(root.left, val, root)
        elif val > root.val:
            self.recurseInsert(root.right, val, root)
        
        
            