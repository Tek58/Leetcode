# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack = [[root, ""]] 
        result = 0 
        
        while stack:
            current, path = stack.pop(0)
            
            if current.left:
                stack.append([current.left, path+str(current.val)])
            if current.right:
                stack.append([current.right, path+str(current.val)])
            
            if not current.left and not current.right:
                path += str(current.val)
                result += int(path, 2)
                
        return result