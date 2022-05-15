# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            res = 0
            for i in range(len(queue)):
                curr = queue.popleft()
                res += curr.val
                if curr.left:
                    queue.append(curr.left)
            
                if curr.right:
                    queue.append(curr.right)
                
        return res
        
                
            
        
        