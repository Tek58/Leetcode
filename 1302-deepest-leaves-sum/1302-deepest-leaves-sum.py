# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest = float("-inf")
        store = defaultdict(int)
        queue = deque([(root, 0)])
        while queue:
            curr, level = queue.pop()
            store[level] += curr.val
            deepest = max(deepest, level)
            if curr.left:
                queue.append((curr.left, level+1))
            
            if curr.right:
                queue.append((curr.right, level+1))
        
        return store[deepest]
        
                
            
        
        