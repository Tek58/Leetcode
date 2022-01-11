# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.path_to_leaf = []
        self.total_binary_sum = 0
        
        def traverse(node, path):
            if node.left:
                traverse(node.left, path+str(node.val))
            if node.right:
                traverse(node.right, path+str(node.val))
            
            if not node.left and not node.right:
                path += str(node.val)
                self.path_to_leaf.append(path)
                self.total_binary_sum += int(path, 2)
        
        traverse(root, "")
        return self.total_binary_sum