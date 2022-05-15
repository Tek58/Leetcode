# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest = float("-inf")
        queue = deque([(root, 0)])
        while queue:
            val, level = queue.pop()
            deepest = max(deepest, level)
            if val.left:
                queue.append((val.left, level+1))
            
            if val.right:
                queue.append((val.right, level+1))
                
        res = 0
        queue = deque([(root, 0)])
        while queue:
            curr, level = queue.pop()
            if level == deepest:
                res += curr.val
            if curr.left:
                queue.append((curr.left, level+1))
            
            if curr.right:
                queue.append((curr.right, level+1))
        
        return res
        
                
            
        
        