# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest = float("-inf")
        res, deepest = root.val, 0
        queue = deque([(root, 0)])
        while queue:
            curr, level = queue.pop()
            if level == deepest:
                res += curr.val
            
            if level > deepest:
                deepest = level
                res = curr.val
                
            if curr.left:
                queue.append((curr.left, level+1))
            
            if curr.right:
                queue.append((curr.right, level+1))
        
        return res
        
                
            
        
        