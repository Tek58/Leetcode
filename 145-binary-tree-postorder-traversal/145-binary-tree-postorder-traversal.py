# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        curr = root
        while stack:
            value = stack.pop()
            result.append(value.val)
            
            if value.left:
                stack.append(value.left)
            if value.right:
                stack.append(value.right)
                
        

        return result[::-1]